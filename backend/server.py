from fastapi import FastAPI, APIRouter, HTTPException, Request, Response
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime, timezone, timedelta
import httpx
import feedparser
import random
from data import GT3_CARS, GT4_CARS, F1_CARS, ALL_TRACKS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

from emergentintegrations.payments.stripe.checkout import StripeCheckout, CheckoutSessionResponse, CheckoutStatusResponse, CheckoutSessionRequest
stripe_api_key = os.environ.get('STRIPE_API_KEY', 'sk_test_emergent')

app = FastAPI()
api_router = APIRouter(prefix="/api")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ============ MODELS ============
class User(BaseModel):
    model_config = ConfigDict(extra="ignore")
    user_id: str
    email: str
    name: str
    picture: Optional[str] = None
    subscription_tier: str = "free"
    subscription_expires: Optional[datetime] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SessionRequest(BaseModel):
    session_id: str

# ============ AUTH HELPERS ============
async def get_current_user(request: Request) -> Optional[User]:
    session_token = request.cookies.get("session_token")
    if not session_token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            session_token = auth_header[7:]
    if not session_token:
        return None
    session_doc = await db.user_sessions.find_one({"session_token": session_token}, {"_id": 0})
    if not session_doc:
        return None
    expires_at = session_doc["expires_at"]
    if isinstance(expires_at, str):
        expires_at = datetime.fromisoformat(expires_at)
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    if expires_at < datetime.now(timezone.utc):
        return None
    user_doc = await db.users.find_one({"user_id": session_doc["user_id"]}, {"_id": 0})
    if not user_doc:
        return None
    return User(**user_doc)

async def require_auth(request: Request) -> User:
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

# ============ AUTH ENDPOINTS ============
@api_router.post("/auth/session")
async def create_session(request: Request, session_req: SessionRequest, response: Response):
    # REMINDER: DO NOT HARDCODE THE URL, OR ADD ANY FALLBACKS OR REDIRECT URLS, THIS BREAKS THE AUTH
    try:
        async with httpx.AsyncClient() as client_http:
            resp = await client_http.get(
                "https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data",
                headers={"X-Session-ID": session_req.session_id}
            )
            if resp.status_code != 200:
                raise HTTPException(status_code=401, detail="Invalid session ID")
            auth_data = resp.json()
    except Exception as e:
        logger.error(f"Auth error: {e}")
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    user_id = f"user_{uuid.uuid4().hex[:12]}"
    session_token = auth_data.get("session_token", f"sess_{uuid.uuid4().hex}")
    
    existing_user = await db.users.find_one({"email": auth_data["email"]}, {"_id": 0})
    if existing_user:
        user_id = existing_user["user_id"]
        await db.users.update_one({"email": auth_data["email"]}, {"$set": {"name": auth_data["name"], "picture": auth_data.get("picture")}})
    else:
        await db.users.insert_one({"user_id": user_id, "email": auth_data["email"], "name": auth_data["name"], "picture": auth_data.get("picture"), "subscription_tier": "free", "subscription_expires": None, "created_at": datetime.now(timezone.utc).isoformat()})
    
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)
    await db.user_sessions.delete_many({"user_id": user_id})
    await db.user_sessions.insert_one({"user_id": user_id, "session_token": session_token, "expires_at": expires_at.isoformat(), "created_at": datetime.now(timezone.utc).isoformat()})
    
    response.set_cookie(key="session_token", value=session_token, httponly=True, secure=True, samesite="none", path="/", max_age=7*24*60*60)
    user = await db.users.find_one({"user_id": user_id}, {"_id": 0})
    return user

@api_router.get("/auth/me")
async def get_me(request: Request):
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user.model_dump()

@api_router.post("/auth/logout")
async def logout(request: Request, response: Response):
    session_token = request.cookies.get("session_token")
    if session_token:
        await db.user_sessions.delete_many({"session_token": session_token})
    response.delete_cookie(key="session_token", path="/", secure=True, samesite="none")
    return {"message": "Logged out"}

# ============ STRIPE ============
SUBSCRIPTION_PRICE = 9.99

@api_router.post("/payments/create-checkout")
async def create_checkout(request: Request):
    body = await request.json()
    origin_url = body.get("origin_url", "")
    user = await get_current_user(request)
    user_id = user.user_id if user else None
    user_email = user.email if user else body.get("email")
    
    host_url = str(request.base_url).rstrip("/")
    webhook_url = f"{host_url}/api/webhook/stripe"
    stripe_checkout = StripeCheckout(api_key=stripe_api_key, webhook_url=webhook_url)
    
    success_url = f"{origin_url}/subscription/success?session_id={{CHECKOUT_SESSION_ID}}"
    cancel_url = f"{origin_url}/subscription"
    metadata = {"user_id": user_id or "", "user_email": user_email or "", "plan": "premium_monthly"}
    
    session: CheckoutSessionResponse = await stripe_checkout.create_checkout_session(
        CheckoutSessionRequest(amount=SUBSCRIPTION_PRICE, currency="usd", success_url=success_url, cancel_url=cancel_url, metadata=metadata)
    )
    
    await db.payment_transactions.insert_one({"transaction_id": f"txn_{uuid.uuid4().hex[:12]}", "user_id": user_id, "user_email": user_email, "session_id": session.session_id, "amount": SUBSCRIPTION_PRICE, "currency": "usd", "metadata": metadata, "payment_status": "pending", "created_at": datetime.now(timezone.utc).isoformat()})
    return {"url": session.url, "session_id": session.session_id}

@api_router.get("/payments/status/{session_id}")
async def get_payment_status(session_id: str, request: Request):
    host_url = str(request.base_url).rstrip("/")
    stripe_checkout = StripeCheckout(api_key=stripe_api_key, webhook_url=f"{host_url}/api/webhook/stripe")
    status: CheckoutStatusResponse = await stripe_checkout.get_checkout_status(session_id)
    
    existing = await db.payment_transactions.find_one({"session_id": session_id}, {"_id": 0})
    if existing and existing.get("payment_status") != "paid" and status.payment_status == "paid":
        await db.payment_transactions.update_one({"session_id": session_id}, {"$set": {"payment_status": "paid", "status": status.status}})
        if existing.get("user_id"):
            await db.users.update_one({"user_id": existing["user_id"]}, {"$set": {"subscription_tier": "premium", "subscription_expires": (datetime.now(timezone.utc) + timedelta(days=30)).isoformat()}})
    
    return {"status": status.status, "payment_status": status.payment_status, "amount_total": status.amount_total, "currency": status.currency}

@api_router.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    body = await request.body()
    signature = request.headers.get("Stripe-Signature")
    host_url = str(request.base_url).rstrip("/")
    stripe_checkout = StripeCheckout(api_key=stripe_api_key, webhook_url=f"{host_url}/api/webhook/stripe")
    try:
        webhook_response = await stripe_checkout.handle_webhook(body, signature)
        if webhook_response.payment_status == "paid":
            existing = await db.payment_transactions.find_one({"session_id": webhook_response.session_id}, {"_id": 0})
            if existing and existing.get("payment_status") != "paid":
                await db.payment_transactions.update_one({"session_id": webhook_response.session_id}, {"$set": {"payment_status": "paid"}})
                if existing.get("user_id"):
                    await db.users.update_one({"user_id": existing["user_id"]}, {"$set": {"subscription_tier": "premium", "subscription_expires": (datetime.now(timezone.utc) + timedelta(days=30)).isoformat()}})
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"status": "error", "message": str(e)}

# ============ TELEMETRY ============
def generate_realistic_telemetry(track_id: str, car_id: str):
    track = None
    for t in ALL_TRACKS:
        if t["track_id"] == track_id:
            track = t
            break
    if not track:
        track = ALL_TRACKS[0]
    
    data_points = []
    track_length_m = track["length_km"] * 1000
    braking_zones = {bp["corner"]: bp for bp in track.get("braking_points", [])}
    
    speed = 280
    throttle = 100
    brake = 0
    gear = 7
    rpm = 10500
    steering = 0
    num_points = int(track_length_m / 10)
    
    for i in range(num_points):
        distance = i * 10
        lap_progress = distance / track_length_m
        in_braking = False
        corner_num = None
        
        for corner in track["corners"]:
            corner_progress = corner["number"] / max(len(track["corners"]), 1)
            if abs(lap_progress - corner_progress) < 0.05:
                in_braking = True
                corner_num = corner["number"]
                target_speed = corner["speed"]
                target_gear = corner["gear"]
                break
        
        if in_braking and corner_num:
            if lap_progress < (corner_num / max(len(track["corners"]), 1)):
                brake = min(100, brake + random.randint(20, 35))
                throttle = max(0, throttle - random.randint(30, 50))
                speed = max(target_speed, speed - random.randint(8, 15))
                gear = max(target_gear, gear - 1) if random.random() > 0.5 else gear
                steering = random.randint(-35, 35)
            else:
                brake = max(0, brake - random.randint(20, 40))
                throttle = min(100, throttle + random.randint(15, 30))
                speed = min(330, speed + random.randint(5, 12))
                gear = min(8, gear + 1) if random.random() > 0.6 and throttle > 70 else gear
                steering = int(steering * 0.7)
        else:
            brake = 0
            throttle = min(100, throttle + random.randint(5, 15))
            speed = min(340, speed + random.randint(2, 8))
            gear = min(8, gear + 1) if speed > 280 and random.random() > 0.8 else gear
            steering = int(steering * 0.5) + random.randint(-5, 5)
        
        speed = max(50, min(350, speed))
        throttle = max(0, min(100, throttle))
        brake = max(0, min(100, brake))
        gear = max(1, min(8, gear))
        rpm = max(6000, min(12500, 8000 + gear * 1200 + random.randint(-300, 300)))
        steering = max(-90, min(90, steering))
        
        data_points.append({
            "distance": distance,
            "speed": speed + random.randint(-2, 2),
            "throttle": throttle,
            "brake": brake,
            "gear": gear,
            "rpm": rpm,
            "steering": steering,
            "lateral_g": round(abs(steering) / 30 * random.uniform(0.8, 1.2), 2),
            "longitudinal_g": round((brake - throttle) / 50 * random.uniform(0.8, 1.2), 2)
        })
    
    return data_points

# ============ TRACK ENDPOINTS ============
@api_router.get("/tracks")
async def get_tracks():
    return ALL_TRACKS

@api_router.get("/tracks/{track_id}")
async def get_track(track_id: str):
    for track in ALL_TRACKS:
        if track["track_id"] == track_id:
            return track
    raise HTTPException(status_code=404, detail="Track not found")

# ============ CAR ENDPOINTS ============
@api_router.get("/cars")
async def get_cars(category: Optional[str] = None, simulator: Optional[str] = None):
    all_cars = F1_CARS + GT3_CARS + GT4_CARS
    if category:
        all_cars = [c for c in all_cars if c["category"].lower() == category.lower()]
    if simulator:
        all_cars = [c for c in all_cars if c.get("simulator", "").lower() == simulator.lower()]
    return all_cars

@api_router.get("/cars/{car_id}")
async def get_car(car_id: str):
    for car in F1_CARS + GT3_CARS + GT4_CARS:
        if car["car_id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")

# ============ TELEMETRY ENDPOINTS ============
@api_router.get("/telemetry/{track_id}/{car_id}")
async def get_telemetry(track_id: str, car_id: str):
    data_points = generate_realistic_telemetry(track_id, car_id)
    neg_g = [abs(dp["longitudinal_g"]) for dp in data_points if dp["longitudinal_g"] < 0]
    return {
        "track_id": track_id,
        "car_id": car_id,
        "lap_number": 1,
        "data_points": data_points,
        "summary": {
            "max_speed": max(dp["speed"] for dp in data_points),
            "avg_speed": round(sum(dp["speed"] for dp in data_points) / len(data_points), 1),
            "max_lateral_g": max(dp["lateral_g"] for dp in data_points),
            "max_braking_g": max(neg_g) if neg_g else 0
        }
    }

# ============ QUIZZES ============
QUIZZES = [
    {"quiz_id":"braking_basics","title":"Braking Fundamentals","category":"technique","difficulty":"beginner","questions":[
        {"id":1,"question":"What is trail braking?","options":["Braking only on straights","Gradually releasing brake while turning in","Using the handbrake","Braking with rear wheels only"],"correct":1,"explanation":"Trail braking gradually releases brake pressure while turning, helping weight transfer and rotation."},
        {"id":2,"question":"Where should most braking be completed?","options":["At the apex","Before the turn-in point","After the apex","During corner exit"],"correct":1,"explanation":"Most braking should be in a straight line before turn-in for optimal grip."},
        {"id":3,"question":"What happens braking while turning at the limit?","options":["Car goes faster","Car understeers or loses grip","Nothing changes","Car gets more grip"],"correct":1,"explanation":"Braking while turning at limit overloads tires, causing understeer or grip loss."},
        {"id":4,"question":"What is threshold braking?","options":["Braking at 50%","Max braking just before lockup","Pumping the brakes","Braking after the corner"],"correct":1,"explanation":"Threshold braking applies max pressure just before wheels lock up."}
    ]},
    {"quiz_id":"racing_lines","title":"Racing Lines Mastery","category":"technique","difficulty":"intermediate","questions":[
        {"id":1,"question":"What is the geometric racing line?","options":["Shortest path","Path allowing highest minimum speed","Following inside edge","Random path"],"correct":1,"explanation":"Geometric line maximizes corner radius for highest speed."},
        {"id":2,"question":"When to use a late apex?","options":["Every corner","When a long straight follows","Only in rain","Never"],"correct":1,"explanation":"Late apex allows earlier throttle and better exit speed."},
        {"id":3,"question":"Advantage of an early apex?","options":["Better exit speed","Better defensive positioning","Always faster","Saves fuel"],"correct":1,"explanation":"Early apex is used defensively or when a slow corner follows."},
        {"id":4,"question":"In a chicane, what determines speed?","options":["Entry speed only","The slowest point","Exit speed only","Random factors"],"correct":1,"explanation":"Chicane speed is limited by the slowest point in the complex."}
    ]},
    {"quiz_id":"f1_tracks","title":"F1 Circuit Knowledge","category":"tracks","difficulty":"intermediate","questions":[
        {"id":1,"question":"Monza's most famous corner?","options":["Lesmo","Parabolica","Variante Ascari","Curva Grande"],"correct":1,"explanation":"Parabolica is Monza's iconic final corner."},
        {"id":2,"question":"Which circuit has Eau Rouge/Raidillon?","options":["Monza","Silverstone","Spa-Francorchamps","Monaco"],"correct":2,"explanation":"Spa-Francorchamps features the legendary Eau Rouge/Raidillon."},
        {"id":3,"question":"What makes Suzuka unique?","options":["Longest circuit","Figure-eight layout","No corners","Only for bikes"],"correct":1,"explanation":"Suzuka is one of few figure-eight layouts."},
        {"id":4,"question":"Monaco's slowest corner?","options":["Sainte Dévote","Grand Hotel Hairpin","Rascasse","Casino"],"correct":1,"explanation":"The Grand Hotel Hairpin is the slowest corner in F1 at ~48 km/h."}
    ]},
    {"quiz_id":"car_setup","title":"Car Setup Basics","category":"engineering","difficulty":"advanced","questions":[
        {"id":1,"question":"Stiffer front ARB does what?","options":["Reduces understeer","Increases understeer","Improves traction","Nothing"],"correct":1,"explanation":"Stiffer front ARB reduces front grip relative to rear, increasing understeer."},
        {"id":2,"question":"Lower tire pressures provide?","options":["More grip but more heat","Less grip","Better top speed","No change"],"correct":0,"explanation":"Lower pressures increase contact patch for more grip but generate more heat."},
        {"id":3,"question":"Negative camber helps with?","options":["Straight-line stability","Cornering grip","Top speed","Fuel efficiency"],"correct":1,"explanation":"Negative camber keeps more tire in contact during cornering roll."},
        {"id":4,"question":"Higher differential preload does?","options":["Loosens the car","More stability on power","Increases top speed","Reduces tire wear"],"correct":1,"explanation":"Higher preload acts more like a locked diff, improving power stability."}
    ]}
]

@api_router.get("/quizzes")
async def get_quizzes():
    return QUIZZES

@api_router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str):
    for q in QUIZZES:
        if q["quiz_id"] == quiz_id:
            return q
    raise HTTPException(status_code=404, detail="Quiz not found")

@api_router.post("/quizzes/{quiz_id}/submit")
async def submit_quiz(quiz_id: str, request: Request):
    body = await request.json()
    answers = body.get("answers", {})
    quiz = next((q for q in QUIZZES if q["quiz_id"] == quiz_id), None)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    correct = 0
    results = []
    for question in quiz["questions"]:
        user_answer = answers.get(str(question["id"]))
        is_correct = user_answer == question["correct"]
        if is_correct:
            correct += 1
        results.append({"question_id": question["id"], "correct": is_correct, "user_answer": user_answer, "correct_answer": question["correct"], "explanation": question["explanation"]})
    
    total = len(quiz["questions"])
    return {"score": correct, "total": total, "percentage": round(correct / total * 100, 1), "results": results}

# ============ NEWS ============
@api_router.get("/news")
async def get_news():
    return [
        {"title":"Verstappen Dominates Spa Qualifying with Record Lap","description":"Max Verstappen set a blistering pace in Belgian GP qualifying, over half a second clear of his nearest rival.","link":"#","published":datetime.now(timezone.utc).isoformat(),"source":"Motorsport News","category":"F1"},
        {"title":"Ferrari Announces Major Aerodynamic Update Package","description":"Scuderia Ferrari will introduce significant updates featuring revised floor edges and new beam wing configurations.","link":"#","published":(datetime.now(timezone.utc)-timedelta(hours=3)).isoformat(),"source":"Formula 1","category":"F1"},
        {"title":"Porsche Takes 1-2 at Spa 24 Hours","description":"The Porsche 992 GT3 R proved its endurance credentials with a dominant 1-2 finish battling changeable weather.","link":"#","published":(datetime.now(timezone.utc)-timedelta(hours=6)).isoformat(),"source":"GT Racing","category":"GT3"},
        {"title":"ACC Update Brings Enhanced Physics","description":"Assetto Corsa Competizione receives refined tire models, improved force feedback, and new content.","link":"#","published":(datetime.now(timezone.utc)-timedelta(hours=10)).isoformat(),"source":"Sim Racing","category":"Sim Racing"},
        {"title":"McLaren MCL38 Development Breakthrough","description":"Technical director explains how McLaren's aggressive development transformed the MCL38 into a championship contender.","link":"#","published":(datetime.now(timezone.utc)-timedelta(hours=14)).isoformat(),"source":"Motorsport Tech","category":"F1"},
        {"title":"iRacing Season 4 with New Tracks","description":"iRacing announces Season 4 with three new laser-scanned circuits and updated GT3 physics.","link":"#","published":(datetime.now(timezone.utc)-timedelta(hours=18)).isoformat(),"source":"Sim Racing","category":"Sim Racing"},
        {"title":"Lamborghini Wins Nürburgring 24 Hours","description":"In a dramatic finish, a Huracán GT3 EVO2 claimed victory after a titanic battle.","link":"#","published":(datetime.now(timezone.utc)-timedelta(days=1)).isoformat(),"source":"Endurance Racing","category":"GT3"},
        {"title":"New 2026 F1 Regulations Finalized","description":"The FIA confirmed final technical regulations for 2026 featuring active aero and new power units.","link":"#","published":(datetime.now(timezone.utc)-timedelta(days=1,hours=5)).isoformat(),"source":"Formula 1","category":"F1"}
    ]

# ============ COMMUNITY ============
@api_router.get("/comments/{entity_type}/{entity_id}")
async def get_comments(entity_type: str, entity_id: str):
    comments = await db.comments.find({"entity_type": entity_type, "entity_id": entity_id}, {"_id": 0}).sort("created_at", -1).to_list(100)
    return comments

@api_router.post("/comments")
async def create_comment(request: Request):
    user = await require_auth(request)
    body = await request.json()
    comment_doc = {"comment_id": f"cmt_{uuid.uuid4().hex[:12]}", "user_id": user.user_id, "user_name": user.name, "content": body.get("content", ""), "entity_type": body.get("entity_type", ""), "entity_id": body.get("entity_id", ""), "created_at": datetime.now(timezone.utc).isoformat()}
    await db.comments.insert_one(comment_doc)
    if "_id" in comment_doc:
        del comment_doc["_id"]
    return comment_doc

# ============ GLOSSARY ============
GLOSSARY = [
    {"term":"Apex","definition":"The innermost point of a corner where the racing line comes closest to the inside."},
    {"term":"DRS","definition":"Drag Reduction System - movable rear wing reducing drag on straights for overtaking."},
    {"term":"Downforce","definition":"Aerodynamic force pushing the car onto the track, increasing grip at the cost of drag."},
    {"term":"Understeer","definition":"When the car turns less than intended, pushing wide. Front tires exceed grip first."},
    {"term":"Oversteer","definition":"When the rear loses grip first, causing extra rotation. Can lead to spins."},
    {"term":"Trail Braking","definition":"Continuing to brake while turning in, gradually releasing pressure for weight transfer."},
    {"term":"Slip Angle","definition":"Angle between tire direction and travel direction. Optimal slip angle maximizes grip."},
    {"term":"Anti-roll Bar","definition":"Suspension component resisting body roll, affecting weight transfer in corners."},
    {"term":"Ride Height","definition":"Distance between car floor and ground. Critical for aero in ground effect cars."},
    {"term":"Brake Bias","definition":"Distribution of braking force between front and rear. Typically 55-60% front."},
    {"term":"Traction Circle","definition":"Concept of total grip available for combined braking, acceleration, and cornering."},
    {"term":"Weight Transfer","definition":"Shift of weight during acceleration, braking, and cornering. Key to fast driving."},
    {"term":"Ground Effect","definition":"Floor generates downforce using Venturi effect, significantly increasing grip."},
    {"term":"Camber","definition":"Wheel angle vs vertical. Negative camber (top inward) improves cornering grip."},
    {"term":"Toe","definition":"Wheel angle vs centerline. Toe-out improves turn-in, toe-in improves straight stability."},
    {"term":"Differential","definition":"Allows wheels to rotate at different speeds. Lock % affects traction and rotation."},
    {"term":"Porpoising","definition":"Bouncing of ground effect cars from downforce-induced bottoming out."},
    {"term":"Sector Times","definition":"Track split into three sectors. Comparing helps identify time loss areas."},
    {"term":"Dirty Air","definition":"Turbulent airflow behind a car reducing aero efficiency for following cars."},
    {"term":"Setup","definition":"All adjustable settings: suspension, aero, differential, tire pressures."}
]

@api_router.get("/glossary")
async def get_glossary():
    return GLOSSARY

# ============ USER PROGRESS ============
@api_router.get("/user/progress")
async def get_user_progress(request: Request):
    user = await require_auth(request)
    progress = await db.user_progress.find_one({"user_id": user.user_id}, {"_id": 0})
    if not progress:
        progress = {"user_id": user.user_id, "completed_quizzes": [], "quiz_scores": {}, "favorite_tracks": [], "favorite_cars": [], "lap_times": {}}
    return progress

@api_router.post("/user/lap-time")
async def save_lap_time(request: Request):
    user = await require_auth(request)
    body = await request.json()
    await db.user_progress.update_one(
        {"user_id": user.user_id},
        {"$set": {f"lap_times.{body.get('track_id')}.{body.get('car_id')}": body.get("lap_time"), "updated_at": datetime.now(timezone.utc).isoformat()}},
        upsert=True
    )
    return {"status": "saved"}

# ============ MAIN ============
@api_router.get("/")
async def root():
    return {"message": "Apex Academy API", "version": "2.0.0", "cars": len(F1_CARS) + len(GT3_CARS) + len(GT4_CARS), "tracks": len(ALL_TRACKS)}

app.include_router(api_router)
app.add_middleware(CORSMiddleware, allow_credentials=True, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
