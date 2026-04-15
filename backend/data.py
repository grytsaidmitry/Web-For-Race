"""
Comprehensive car and track database for Apex Academy.
All cars from ACC, iRacing, F1 25. All tracks from F1 25, ACC, iRacing.
"""

# ============ IMAGE URLS (consistent format) ============
# Car images: action shots on track
# Track images: aerial/scenic views

CAR_IMAGES = {
    # GT3
    "ferrari_296_gt3": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Ferrari_296_GT3_2023.jpg",
    "porsche_992_gt3_r": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Porsche_911_GT3_R_992.jpg",
    "lamborghini_huracan_gt3_evo2": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Lamborghini_Huracan_GT3_EVO2.jpg",
    "mclaren_720s_gt3_evo": "https://upload.wikimedia.org/wikipedia/commons/6/69/McLaren_720S_GT3_Evo.jpg",
    "bmw_m4_gt3": "https://upload.wikimedia.org/wikipedia/commons/2/2c/BMW_M4_GT3.jpg",
    "mercedes_amg_gt3_evo": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Mercedes-AMG_GT3_Evo.jpg",
    "aston_martin_vantage_gt3": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Aston_Martin_Vantage_GT3.jpg",
    "audi_r8_lms_gt3_evo2": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Audi_R8_LMS_GT3_Evo_II.jpg",
    "corvette_z06_gt3r": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Corvette_Z06_GT3R.jpg",
    "nissan_gtr_nismo_gt3": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Nissan_GT-R_NISMO_GT3.jpg",
    "honda_nsx_gt3_evo": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Honda_NSX_GT3_Evo.jpg",
    "bentley_continental_gt3": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Bentley_Continental_GT3.jpg",
    "lexus_rcf_gt3": "https://upload.wikimedia.org/wikipedia/commons/6/60/Lexus_RC_F_GT3.jpg",
    "ford_mustang_gt3": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Ford_Mustang_GT3_2024.jpg",
    
    # GT4
    "porsche_718_cayman_gt4": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Porsche_718_Cayman_GT4_Clubsport.jpg",
    "bmw_m4_gt4": "https://upload.wikimedia.org/wikipedia/commons/3/3e/BMW_M4_GT4.jpg",
    "mclaren_570s_gt4": "https://upload.wikimedia.org/wikipedia/commons/1/1c/McLaren_570S_GT4.jpg",
    "mercedes_amg_gt4": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Mercedes-AMG_GT4.jpg",
    "aston_martin_vantage_gt4": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Aston_Martin_Vantage_GT4.jpg",
    "alpine_a110_gt4": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Alpine_A110_GT4.jpg",
    "audi_r8_lms_gt4": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Audi_R8_LMS_GT4.jpg",
    "chevrolet_camaro_gt4r": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Chevrolet_Camaro_GT4.R.jpg",
    "ktm_xbow_gt4": "https://upload.wikimedia.org/wikipedia/commons/8/87/KTM_X-Bow_GT4.jpg",
    "maserati_mc_gt4": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Maserati_MC20_GT4.jpg",
    "ginetta_g56_gt4": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Ginetta_G56_GT4.jpg",
}

TRACK_IMAGES = {
    "monza": "https://images.unsplash.com/photo-1760456014978-096fc0f3f934?w=800&fit=crop",
    "spa": "https://images.unsplash.com/photo-1695227667420-6af83966b3bf?w=800&fit=crop",
    "silverstone": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "nurburgring_gp": "https://images.unsplash.com/photo-1619976215249-0e2f6679f90f?w=800&fit=crop",
    "suzuka": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&fit=crop",
    "imola": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "barcelona": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "zandvoort": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "monaco": "https://images.unsplash.com/photo-1656337449909-141091f4df4a?w=800&fit=crop",
    "bahrain": "https://images.unsplash.com/photo-1743580838686-6e069965d5cf?w=800&fit=crop",
    "jeddah": "https://images.unsplash.com/photo-1519445950492-d98b9bf804b3?w=800&fit=crop",
    "melbourne": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "shanghai": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "miami": "https://images.unsplash.com/photo-1519445950492-d98b9bf804b3?w=800&fit=crop",
    "montreal": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "red_bull_ring": "https://images.unsplash.com/photo-1746433444303-f8e1dfdac12a?w=800&fit=crop",
    "hungaroring": "https://images.unsplash.com/photo-1619976215249-0e2f6679f90f?w=800&fit=crop",
    "singapore": "https://images.unsplash.com/photo-1707045138754-c636e8c41878?w=800&fit=crop",
    "cota": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "mexico": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "interlagos": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "las_vegas": "https://images.unsplash.com/photo-1519445950492-d98b9bf804b3?w=800&fit=crop",
    "lusail": "https://images.unsplash.com/photo-1743580838686-6e069965d5cf?w=800&fit=crop",
    "yas_marina": "https://images.unsplash.com/photo-1743580838686-6e069965d5cf?w=800&fit=crop",
    "baku": "https://images.unsplash.com/photo-1519445950492-d98b9bf804b3?w=800&fit=crop",
    "misano": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "paul_ricard": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "brands_hatch": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "kyalami": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "bathurst": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "laguna_seca": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "watkins_glen": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
    "indianapolis": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&fit=crop",
    "donington": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "oulton_park": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "snetterton": "https://images.unsplash.com/photo-1612438214708-f428a707dd4e?w=800&fit=crop",
    "valencia": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&fit=crop",
}

# ============ HELPER: create car entry ============
def _car(car_id, name, cat, mfr, year, top_spd, hp, wt, drive, engine, desc, sim, handling, img_key, aero_f, aero_r, aero_desc, susp_farb, susp_rarb, susp_rhf, susp_rhr, tp_f, tp_r, bb, diff_pre, diff_pwr, diff_cst):
    return {
        "car_id": car_id,
        "name": name,
        "category": cat,
        "manufacturer": mfr,
        "year": year,
        "top_speed": top_spd,
        "power_hp": hp,
        "weight_kg": wt,
        "drivetrain": drive,
        "engine": engine,
        "description": desc,
        "image_url": CAR_IMAGES.get(img_key, CAR_IMAGES.get(car_id, "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800")),
        "simulator": sim,
        "handling_characteristics": handling,
        "setup_tips": {
            "aero": {"front_wing": aero_f, "rear_wing": aero_r, "description": aero_desc},
            "suspension": {"front_arb": susp_farb, "rear_arb": susp_rarb, "ride_height_front": susp_rhf, "ride_height_rear": susp_rhr},
            "tires": {"pressure_front": tp_f, "pressure_rear": tp_r},
            "brake_bias": bb,
            "differential": {"preload": diff_pre, "power": diff_pwr, "coast": diff_cst}
        }
    }

# ============ GT3 CARS (ACC + iRacing) ============
GT3_CARS = [
    _car("ferrari_296_gt3","Ferrari 296 GT3","GT3","Ferrari",2023,295,600,1250,"RWD","3.0L Twin-Turbo V6","Successor to the 488 GT3 with hybrid-derived V6. Exceptional mid-corner stability and strong traction.","ACC","Neutral with slight understeer. Very predictable at the limit.","ferrari_296_gt3",5,6,"Balanced setup. Increase rear for stability.",3,5,53,58,27.5,27.3,56.5,40,65,30),
    _car("porsche_992_gt3_r","Porsche 911 GT3 R (992)","GT3","Porsche",2023,292,565,1260,"RWD","4.2L Flat-6 NA","Latest 911 for GT racing. Rear-engine layout provides unique handling requiring driver adaptation.","ACC","Rear-biased weight. Requires smooth inputs. Exceptional exit traction.","porsche_992_gt3_r",7,5,"More front aero to balance rear weight.",4,2,55,55,27.6,27.0,54.0,35,55,25),
    _car("lamborghini_huracan_gt3_evo2","Lamborghini Huracán GT3 EVO2","GT3","Lamborghini",2023,298,585,1245,"RWD","5.2L V10 NA","V10 naturally aspirated with incredible soundtrack. Sharp turn-in and aggressive character.","ACC","Sharp turn-in with potential oversteer on power. Rewards aggressive driving.","lamborghini_huracan_gt3_evo2",4,7,"Rear-heavy aero for stability on power.",5,4,52,57,27.4,27.5,55.5,45,70,35),
    _car("mclaren_720s_gt3_evo","McLaren 720S GT3 EVO","GT3","McLaren",2023,300,590,1240,"RWD","4.0L Twin-Turbo V8","Carbon monocoque with excellent straight-line speed. Best on fast circuits.","ACC","Low drag, high top speed. Precise brake management needed.","mclaren_720s_gt3_evo",6,5,"Low drag for high-speed tracks.",3,4,54,56,27.3,27.4,56.0,38,62,28),
    _car("bmw_m4_gt3","BMW M4 GT3","GT3","BMW",2023,293,590,1265,"RWD","3.0L Twin-Turbo I6","Replaced M6 GT3. Strong mid-range with excellent mechanical grip.","ACC","Predictable, forgiving at the limit. Good for all skill levels.","bmw_m4_gt3",5,6,"Neutral for predictable handling.",4,5,53,57,27.5,27.4,55.0,42,65,32),
    _car("mercedes_amg_gt3_evo","Mercedes-AMG GT3 EVO","GT3","Mercedes-AMG",2023,296,580,1255,"RWD","6.3L V8 NA","Front-mid engine with hand-built AMG V8. Excellent braking stability.","ACC","Front-heavy, requires trail braking. Stable under braking.","mercedes_amg_gt3_evo",4,6,"Front weight helps braking stability.",4,4,54,56,27.4,27.3,55.5,40,60,30),
    _car("aston_martin_vantage_gt3","Aston Martin Vantage GT3","GT3","Aston Martin",2023,291,575,1270,"RWD","4.0L Twin-Turbo V8","British elegance meets AMG power. Balanced chassis rewards smooth driving.","ACC","Balanced. Requires smooth inputs for best results.","aston_martin_vantage_gt3",5,5,"Balance is key for this chassis.",4,5,54,57,27.5,27.4,56.0,40,63,30),
    _car("audi_r8_lms_gt3_evo2","Audi R8 LMS GT3 EVO II","GT3","Audi",2023,294,585,1250,"RWD","5.2L V10 NA","Mid-engine V10 shared with Lamborghini but different character. Strong traction.","ACC","Linear power delivery. Excellent for consistency.","audi_r8_lms_gt3_evo2",5,6,"Slightly rear-biased for traction.",4,4,53,56,27.4,27.5,55.0,42,68,32),
    _car("corvette_z06_gt3r","Chevrolet Corvette Z06 GT3.R","GT3","Chevrolet",2024,297,595,1245,"RWD","5.5L Flat-Plane V8 NA","First mid-engine Corvette racer. Revolutionary American GT power.","iRacing","American muscle with European handling. Aggressive but manageable.","corvette_z06_gt3r",5,6,"Balanced aero for all-round performance.",4,5,53,57,27.4,27.3,55.5,40,65,30),
    _car("nissan_gtr_nismo_gt3","Nissan GT-R NISMO GT3","GT3","Nissan",2023,290,570,1280,"RWD","3.8L Twin-Turbo V6","Based on the legendary GT-R. Converted to RWD but retains iconic character.","ACC","Front-heavy. Careful throttle on exit needed.","nissan_gtr_nismo_gt3",6,6,"Higher front aero for front weight.",5,4,55,56,27.5,27.2,54.5,45,60,28),
    _car("honda_nsx_gt3_evo","Honda NSX GT3 EVO","GT3","Honda",2022,289,560,1270,"RWD","3.5L Twin-Turbo V6","Mid-engine hybrid supercar DNA. Exceptional aero efficiency and balance.","ACC","Very balanced. Excellent high-speed stability.","honda_nsx_gt3_evo",5,5,"Already balanced. Focus on mechanical grip.",4,4,53,55,27.3,27.3,55.5,38,62,30),
    _car("bentley_continental_gt3","Bentley Continental GT3","GT3","Bentley",2022,288,570,1300,"RWD","4.0L Twin-Turbo V8","Heaviest GT3 car but massive stability. Torque-rich power delivery.","ACC","Heavy but planted. Excellent in wet conditions.","bentley_continental_gt3",5,7,"More rear aero compensates for weight.",5,5,55,58,27.6,27.4,56.5,48,68,35),
    _car("lexus_rcf_gt3","Lexus RC F GT3","GT3","Lexus",2022,291,560,1275,"RWD","5.0L V8 NA","Japanese luxury meets GT racing. Naturally aspirated V8 with smooth power.","iRacing","Front-engine with progressive handling. Good tire wear.","lexus_rcf_gt3",4,6,"More rear for front-engine balance.",5,4,54,57,27.4,27.3,55.0,40,62,30),
    _car("ford_mustang_gt3","Ford Mustang GT3","GT3","Ford",2024,294,580,1255,"RWD","5.0L V8 NA","The Mustang enters GT3. American icon with proper race credentials.","ACC","Front-engine muscle. Strong straight-line speed.","ford_mustang_gt3",4,6,"Rear aero for stability on power.",5,4,54,57,27.5,27.3,56.0,42,65,32),
]

# ============ GT4 CARS (ACC) ============
GT4_CARS = [
    _car("porsche_718_cayman_gt4","Porsche 718 Cayman GT4 Clubsport MR","GT4","Porsche",2022,265,425,1320,"RWD","3.8L Flat-6 NA","Mid-engine benchmark GT4. Natural handling and great balance for learning.","ACC","Mid-engine balance. Progressive at the limit. Great for learning.","porsche_718_cayman_gt4",4,5,"Slightly rear-biased for stability.",3,4,55,58,27.0,26.8,54.5,35,55,25),
    _car("bmw_m4_gt4","BMW M4 GT4","GT4","BMW",2022,268,430,1340,"RWD","3.0L Twin-Turbo I6","Excellent low-end torque. Forgiving handling ideal for beginners.","ACC","Front-engine, predictable understeer. Strong braking stability.","bmw_m4_gt4",5,5,"Neutral setup works well across all tracks.",4,4,54,56,27.2,27.0,55.0,40,60,28),
    _car("mclaren_570s_gt4","McLaren 570S GT4","GT4","McLaren",2022,272,445,1310,"RWD","3.8L Twin-Turbo V8","Carbon tub chassis. Lightweight and extremely responsive.","ACC","Sharp turn-in. Potential snap oversteer. Rewards skill.","mclaren_570s_gt4",6,5,"More front aero for turn-in stability.",3,5,52,55,27.1,27.0,55.5,35,58,25),
    _car("mercedes_amg_gt4","Mercedes-AMG GT4","GT4","Mercedes-AMG",2022,270,440,1350,"RWD","4.0L Twin-Turbo V8","Front-engine with powerful twin-turbo V8. Strong on straights.","ACC","Front-heavy. Excellent braking. Patient corner entry needed.","mercedes_amg_gt4",4,6,"More rear aero for front weight balance.",5,4,55,57,27.3,27.1,56.0,42,62,30),
    _car("aston_martin_vantage_gt4","Aston Martin Vantage AMR GT4","GT4","Aston Martin",2022,267,435,1360,"RWD","4.0L Twin-Turbo V8","British GT4 with AMG power. Good balance and reliable.","ACC","Balanced front-engine. Predictable and consistent.","aston_martin_vantage_gt4",5,5,"Neutral setup suits this car best.",4,4,54,56,27.2,27.0,55.5,38,60,28),
    _car("alpine_a110_gt4","Alpine A110 GT4","GT4","Alpine",2022,260,340,1170,"RWD","1.8L Turbo I4","Lightest GT4 car. Mid-engine French sports car. Exceptional agility.","ACC","Extremely nimble. Low power but low weight. Great in tight sections.","alpine_a110_gt4",4,5,"Maximize downforce for lower power.",3,3,52,54,26.8,26.6,54.0,30,50,22),
    _car("audi_r8_lms_gt4","Audi R8 LMS GT4","GT4","Audi",2022,270,440,1330,"RWD","5.2L V10 NA","Mid-engine V10 GT4. Excellent traction with linear power delivery.","ACC","Strong traction. Predictable and forgiving character.","audi_r8_lms_gt4",5,5,"Balanced setup with slight rear bias.",4,4,53,56,27.2,27.1,55.0,40,60,28),
    _car("chevrolet_camaro_gt4r","Chevrolet Camaro GT4.R","GT4","Chevrolet",2022,266,440,1360,"RWD","6.2L V8 NA","American muscle in GT4 form. Torque-rich NA V8.","ACC","Front-engine muscle. Strong straight-line speed.","chevrolet_camaro_gt4r",4,6,"More rear for front weight balance.",5,4,55,57,27.3,27.1,55.5,42,62,30),
    _car("ktm_xbow_gt4","KTM X-BOW GT4","GT4","KTM",2022,258,365,1048,"RWD","2.0L Turbo I4","Lightweight carbon monoframe. Like driving a prototype. Pure race car.","ACC","Ultra-lightweight. Very direct feel. Needs smooth inputs.","ktm_xbow_gt4",5,5,"Balanced for maximum mechanical grip.",3,3,50,52,26.5,26.3,53.5,30,52,22),
    _car("maserati_mc_gt4","Maserati MC GT4","GT4","Maserati",2022,264,420,1340,"RWD","3.0L Twin-Turbo V6","Italian GT4 with MC20 DNA. Strong in mid-speed corners.","ACC","Balanced mid-engine. Good in technical sections.","maserati_mc_gt4",5,5,"Neutral for best versatility.",4,4,53,55,27.0,26.8,54.5,38,58,26),
    _car("ginetta_g56_gt4","Ginetta G56 GT4","GT4","Ginetta",2022,262,410,1300,"RWD","3.7L V6 NA","British lightweight racer. Designed purely for track performance.","ACC","Lightweight and agile. Responsive chassis.","ginetta_g56_gt4",5,5,"Balanced for all-round performance.",3,4,53,55,26.9,26.7,54.0,35,55,25),
]

# ============ F1 CARS (F1 25) ============
F1_CARS = [
    _car("red_bull_rb20","Red Bull RB20","F1","Red Bull Racing",2024,370,1000,798,"RWD","Honda RBPT 1.6L V6 Turbo Hybrid","Dominant 2024 car. Exceptional aero efficiency with refined ground effect.","F1 25","Planted rear. Exceptional traction. Precise front end needed.","red_bull_rb20",25,30,"Very sensitive to front wing.",7,5,24,45,24.0,22.5,56.0,40,65,55),
    _car("mercedes_w15","Mercedes W15","F1","Mercedes-AMG",2024,368,1000,798,"RWD","Mercedes 1.6L V6 Turbo Hybrid","Return to form. Strong on high-speed circuits with improved rear stability.","F1 25","Good mechanical grip. Strong in medium-speed corners.","mercedes_w15",27,28,"Works well with lower rear wing.",6,6,25,44,23.8,22.3,55.5,38,60,52),
    _car("ferrari_sf24","Ferrari SF-24","F1","Scuderia Ferrari",2024,369,1000,798,"RWD","Ferrari 066/12 1.6L V6 Turbo Hybrid","Aggressive design with strong qualifying pace. Sharp front end.","F1 25","Sharp front. Can be nervous at high speed. Excellent traction.","ferrari_sf24",26,32,"Prefers higher rear downforce.",5,7,26,46,24.2,22.8,56.5,42,68,58),
    _car("mclaren_mcl38","McLaren MCL38","F1","McLaren",2024,367,1000,798,"RWD","Mercedes 1.6L V6 Turbo Hybrid","Papaya power. Excellent tire management and consistent race pace.","F1 25","Very balanced. Good in all corner types. Excellent tire preservation.","mclaren_mcl38",28,29,"Balanced approach works best.",6,6,25,45,23.9,22.4,55.0,40,62,54),
    _car("aston_martin_amr24","Aston Martin AMR24","F1","Aston Martin",2024,366,1000,798,"RWD","Mercedes 1.6L V6 Turbo Hybrid","Strong low-speed grip with improved aero efficiency.","F1 25","Good low-speed grip. Excellent braking stability.","aston_martin_amr24",29,31,"Higher downforce for stability.",5,6,26,46,24.0,22.6,56.0,40,64,55),
    _car("alpine_a524","Alpine A524","F1","Alpine",2024,365,1000,798,"RWD","Renault E-Tech RE24 1.6L V6 Turbo Hybrid","Mid-pack challenger with improved power unit. Competitive in qualifying.","F1 25","Decent balance. Struggles in high-speed sections.","alpine_a524",27,30,"Moderate downforce for best balance.",6,6,25,45,24.0,22.5,55.5,38,60,52),
    _car("williams_fw46","Williams FW46","F1","Williams",2024,369,1000,798,"RWD","Mercedes 1.6L V6 Turbo Hybrid","Fastest in a straight line. Low drag philosophy with Mercedes power.","F1 25","Low drag, high top speed. Struggles in slow corners.","williams_fw46",24,26,"Low drag for straight-line advantage.",5,5,24,44,23.5,22.0,55.0,35,58,50),
    _car("rb_vcarb01","Visa Cash App RB VCARB 01","F1","RB",2024,367,1000,798,"RWD","Honda RBPT 1.6L V6 Turbo Hybrid","Red Bull's junior team. Solid midfield contender with good development rate.","F1 25","Balanced midfield car. Good driver feedback.","rb_vcarb01",26,29,"Neutral setup for consistency.",6,6,25,45,23.8,22.3,55.5,38,62,54),
    _car("sauber_c44","Sauber C44","F1","Sauber",2024,364,1000,798,"RWD","Ferrari 066/12 1.6L V6 Turbo Hybrid","Technical development ongoing. Improved over previous year.","F1 25","Predictable handling. Good in medium-speed corners.","sauber_c44",27,30,"Balanced for consistency.",6,6,25,45,24.0,22.5,55.5,38,60,52),
    _car("haas_vf24","Haas VF-24","F1","Haas",2024,366,1000,798,"RWD","Ferrari 066/12 1.6L V6 Turbo Hybrid","Competitive in qualifying trim. Strong tire management.","F1 25","Good single-lap pace. Tire management is key.","haas_vf24",27,30,"Moderate downforce for race pace.",6,6,25,45,24.0,22.5,55.5,40,62,54),
]

# ============ TRACKS ============
def _track(tid, name, country, length, turns, drs, record, holder, desc, cats, corners, braking, sims):
    return {
        "track_id": tid,
        "name": name,
        "country": country,
        "length_km": length,
        "turns": turns,
        "drs_zones": drs,
        "lap_record": record,
        "lap_record_holder": holder,
        "description": desc,
        "image_url": TRACK_IMAGES.get(tid, "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800"),
        "categories": cats,
        "simulators": sims,
        "corners": corners,
        "braking_points": braking,
    }

# F1 25 + ACC + iRacing tracks
ALL_TRACKS = [
    _track("monza","Autodromo Nazionale Monza","Italy",5.793,11,2,"1:21.046","Rubens Barrichello","The Temple of Speed. Features long straights and challenging chicanes demanding precision braking.",["F1","GT3","GT4"],[
        {"number":1,"name":"Variante del Rettifilo","type":"chicane","speed":80,"gear":2,"difficulty":"medium","notes":"Heavy braking zone from 340 km/h. Hit first apex tight, open to second."},
        {"number":2,"name":"Curva Grande","type":"fast","speed":260,"gear":7,"difficulty":"high","notes":"Flat out in dry. Slight lift in wet. Use all track width."},
        {"number":3,"name":"Variante della Roggia","type":"chicane","speed":75,"gear":2,"difficulty":"medium","notes":"Late braking possible. Good exit for back straight."},
        {"number":4,"name":"Lesmo 1","type":"medium","speed":180,"gear":4,"difficulty":"high","notes":"Blind entry. Commit to apex. Very punishing if you run wide."},
        {"number":5,"name":"Lesmo 2","type":"medium","speed":165,"gear":4,"difficulty":"high","notes":"Tighter than Lesmo 1. Late apex for better exit."},
        {"number":6,"name":"Variante Ascari","type":"chicane","speed":210,"gear":5,"difficulty":"very high","notes":"High-speed chicane. Rhythm is key."},
        {"number":7,"name":"Curva Parabolica","type":"fast","speed":240,"gear":6,"difficulty":"very high","notes":"Long constant radius. Late apex crucial for main straight speed."}
    ],[
        {"corner":1,"marker":"150m","distance_m":125,"initial_speed":340,"target_speed":80,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"},
        {"corner":3,"marker":"100m","distance_m":85,"initial_speed":260,"target_speed":75,"brake_pressure":95,"downshift":"7-6-5-4-3-2"},
        {"corner":4,"marker":"100m","distance_m":90,"initial_speed":310,"target_speed":180,"brake_pressure":85,"downshift":"8-7-6-5-4"},
        {"corner":5,"marker":"75m","distance_m":70,"initial_speed":240,"target_speed":165,"brake_pressure":80,"downshift":"6-5-4"},
        {"corner":6,"marker":"100m","distance_m":95,"initial_speed":330,"target_speed":210,"brake_pressure":75,"downshift":"8-7-6-5"},
        {"corner":7,"marker":"50m","distance_m":45,"initial_speed":310,"target_speed":240,"brake_pressure":60,"downshift":"7-6"}
    ],["F1 25","ACC","iRacing"]),
    _track("spa","Circuit de Spa-Francorchamps","Belgium",7.004,19,2,"1:46.286","Valtteri Bottas","The most challenging circuit. Dramatic elevation, unpredictable weather, legendary Eau Rouge/Raidillon.",["F1","GT3","GT4"],[
        {"number":1,"name":"La Source","type":"hairpin","speed":65,"gear":2,"difficulty":"low","notes":"Slow hairpin. Late apex for good exit speed."},
        {"number":2,"name":"Eau Rouge","type":"fast","speed":290,"gear":7,"difficulty":"very high","notes":"Flat in qualifying. Requires commitment and perfect line."},
        {"number":3,"name":"Raidillon","type":"fast","speed":280,"gear":7,"difficulty":"very high","notes":"Blind crest. Trust your line. Car gets light at the top."},
        {"number":4,"name":"Les Combes","type":"chicane","speed":110,"gear":3,"difficulty":"medium","notes":"Hard braking zone. Good overtaking opportunity."},
        {"number":5,"name":"Malmedy","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Double apex. Smooth inputs essential."},
        {"number":6,"name":"Rivage","type":"hairpin","speed":85,"gear":2,"difficulty":"medium","notes":"Downhill hairpin. Easy to lock up on entry."},
        {"number":7,"name":"Pouhon","type":"double apex","speed":260,"gear":6,"difficulty":"very high","notes":"High-speed double apex. Flat if you nail the entry."},
        {"number":8,"name":"Fagnes","type":"chicane","speed":90,"gear":3,"difficulty":"low","notes":"Slow chicane. Set up for Stavelot."},
        {"number":9,"name":"Stavelot","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Double right. Early turn-in, late second apex."},
        {"number":10,"name":"Blanchimont","type":"fast","speed":295,"gear":7,"difficulty":"very high","notes":"Flat out. Slight lift in wet."},
        {"number":11,"name":"Bus Stop","type":"chicane","speed":75,"gear":2,"difficulty":"medium","notes":"Heavy braking. Critical for lap time."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":310,"target_speed":65,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"},
        {"corner":4,"marker":"150m","distance_m":140,"initial_speed":290,"target_speed":110,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":6,"marker":"100m","distance_m":90,"initial_speed":220,"target_speed":85,"brake_pressure":90,"downshift":"5-4-3-2"},
        {"corner":8,"marker":"75m","distance_m":70,"initial_speed":260,"target_speed":90,"brake_pressure":95,"downshift":"6-5-4-3"},
        {"corner":11,"marker":"150m","distance_m":135,"initial_speed":320,"target_speed":75,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"}
    ],["F1 25","ACC","iRacing"]),
    _track("silverstone","Silverstone Circuit","United Kingdom",5.891,18,2,"1:27.097","Max Verstappen","Home of British motorsport. Fast flowing circuit with the legendary Maggots-Becketts-Chapel.",["F1","GT3","GT4"],[
        {"number":1,"name":"Abbey","type":"fast","speed":275,"gear":6,"difficulty":"high","notes":"Fast right. Flat or slight lift depending on setup."},
        {"number":3,"name":"Village","type":"slow","speed":100,"gear":3,"difficulty":"medium","notes":"Tight corner. Good exit for The Loop."},
        {"number":4,"name":"The Loop","type":"hairpin","speed":80,"gear":2,"difficulty":"medium","notes":"Switchback. Setup for exit speed."},
        {"number":6,"name":"Brooklands","type":"slow","speed":90,"gear":2,"difficulty":"medium","notes":"Heavy braking from Wellington Straight."},
        {"number":7,"name":"Luffield","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Long corner. Critical exit for straight."},
        {"number":9,"name":"Copse","type":"fast","speed":265,"gear":7,"difficulty":"very high","notes":"One of fastest corners in F1. Flat with good setup."},
        {"number":10,"name":"Maggots","type":"fast","speed":280,"gear":7,"difficulty":"very high","notes":"Start of the complex. Flat throughout."},
        {"number":11,"name":"Becketts","type":"fast","speed":245,"gear":6,"difficulty":"very high","notes":"Rapid direction changes. Requires rhythm."},
        {"number":12,"name":"Chapel","type":"fast","speed":290,"gear":7,"difficulty":"high","notes":"Exit of complex onto Hangar Straight."},
        {"number":13,"name":"Stowe","type":"medium","speed":155,"gear":4,"difficulty":"high","notes":"Heavy braking. Good overtaking spot."},
        {"number":15,"name":"Club","type":"slow","speed":110,"gear":3,"difficulty":"medium","notes":"Final corner. Exit speed is crucial."}
    ],[
        {"corner":3,"marker":"100m","distance_m":90,"initial_speed":290,"target_speed":100,"brake_pressure":90,"downshift":"7-6-5-4-3"},
        {"corner":6,"marker":"125m","distance_m":115,"initial_speed":290,"target_speed":90,"brake_pressure":95,"downshift":"8-7-6-5-4-3-2"},
        {"corner":13,"marker":"100m","distance_m":95,"initial_speed":315,"target_speed":155,"brake_pressure":85,"downshift":"8-7-6-5-4"},
        {"corner":15,"marker":"75m","distance_m":65,"initial_speed":195,"target_speed":110,"brake_pressure":80,"downshift":"4-3"}
    ],["F1 25","ACC","iRacing"]),
    _track("monaco","Circuit de Monaco","Monaco",3.337,19,1,"1:10.166","Lewis Hamilton","The crown jewel of motorsport. Tight street circuit with zero margin for error.",["F1"],[
        {"number":1,"name":"Sainte Dévote","type":"medium","speed":110,"gear":3,"difficulty":"high","notes":"First corner after start. Tight right with wall close."},
        {"number":3,"name":"Massenet","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Left-hander going uphill. Leads to Casino."},
        {"number":4,"name":"Casino","type":"medium","speed":155,"gear":4,"difficulty":"high","notes":"Blind crest at entry. Walls close on both sides."},
        {"number":5,"name":"Mirabeau Haute","type":"slow","speed":70,"gear":2,"difficulty":"medium","notes":"Setup for the Grand Hotel Hairpin."},
        {"number":6,"name":"Grand Hotel Hairpin","type":"hairpin","speed":48,"gear":1,"difficulty":"high","notes":"Slowest corner in F1. Extremely tight."},
        {"number":8,"name":"Portier","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Right-hander into the tunnel."},
        {"number":9,"name":"Tunnel","type":"fast","speed":255,"gear":6,"difficulty":"high","notes":"Light changes dramatically. Flat through."},
        {"number":10,"name":"Nouvelle Chicane","type":"chicane","speed":70,"gear":2,"difficulty":"medium","notes":"Heavy braking from tunnel speed."},
        {"number":12,"name":"Tabac","type":"medium","speed":145,"gear":4,"difficulty":"very high","notes":"Fast corner with wall on exit. No margin."},
        {"number":15,"name":"Piscine","type":"chicane","speed":100,"gear":3,"difficulty":"high","notes":"Swimming pool chicane. Quick direction change."},
        {"number":18,"name":"Rascasse","type":"hairpin","speed":50,"gear":1,"difficulty":"medium","notes":"Tight hairpin. Easy to make contact."},
        {"number":19,"name":"Anthony Noghes","type":"slow","speed":65,"gear":2,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"50m","distance_m":45,"initial_speed":280,"target_speed":110,"brake_pressure":100,"downshift":"7-6-5-4-3"},
        {"corner":6,"marker":"50m","distance_m":40,"initial_speed":120,"target_speed":48,"brake_pressure":90,"downshift":"3-2-1"},
        {"corner":10,"marker":"100m","distance_m":95,"initial_speed":255,"target_speed":70,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":18,"marker":"50m","distance_m":40,"initial_speed":130,"target_speed":50,"brake_pressure":95,"downshift":"3-2-1"}
    ],["F1 25"]),
    _track("bahrain","Bahrain International Circuit","Bahrain",5.412,15,3,"1:31.447","Pedro de la Rosa","The desert circuit that opens the F1 season. Night race with excellent overtaking opportunities.",["F1"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":150,"gear":4,"difficulty":"medium","notes":"Good overtaking spot. Late braking possible."},
        {"number":4,"name":"Turn 4","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Tight right-hander. Exit speed matters."},
        {"number":8,"name":"Turn 8","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Slow corner leading onto back straight."},
        {"number":10,"name":"Turn 10","type":"medium","speed":185,"gear":5,"difficulty":"high","notes":"High-speed right. Tests downforce."},
        {"number":11,"name":"Turn 11","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Setup for Turn 12-13."},
        {"number":14,"name":"Turn 14","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Leads onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":310,"target_speed":150,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":4,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":75,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":10,"marker":"50m","distance_m":45,"initial_speed":280,"target_speed":185,"brake_pressure":70,"downshift":"7-6-5"},
        {"corner":14,"marker":"75m","distance_m":65,"initial_speed":220,"target_speed":155,"brake_pressure":75,"downshift":"5-4"}
    ],["F1 25"]),
    _track("red_bull_ring","Red Bull Ring","Austria",4.318,10,2,"1:05.619","Carlos Sainz","Short, fast lap with dramatic elevation. Three heavy braking zones and stunning mountain backdrop.",["F1","GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Heavy braking uphill. Good overtaking spot."},
        {"number":3,"name":"Turn 3","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Heavy braking downhill. Tricky entry."},
        {"number":4,"name":"Turn 4","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Right-hander leading to Turn 5."},
        {"number":6,"name":"Turn 6","type":"fast","speed":225,"gear":5,"difficulty":"high","notes":"Fast right-hander over crest."},
        {"number":7,"name":"Turn 7","type":"fast","speed":230,"gear":5,"difficulty":"high","notes":"Fast left. Flat in F1."},
        {"number":9,"name":"Turn 9","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Penultimate corner. Exit speed matters."},
        {"number":10,"name":"Turn 10","type":"slow","speed":100,"gear":3,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":320,"target_speed":80,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"},
        {"corner":3,"marker":"100m","distance_m":85,"initial_speed":280,"target_speed":85,"brake_pressure":95,"downshift":"7-6-5-4-3-2"},
        {"corner":4,"marker":"50m","distance_m":40,"initial_speed":150,"target_speed":90,"brake_pressure":75,"downshift":"4-3"},
        {"corner":9,"marker":"75m","distance_m":65,"initial_speed":230,"target_speed":80,"brake_pressure":95,"downshift":"5-4-3-2"}
    ],["F1 25","ACC","iRacing"]),
    _track("suzuka","Suzuka International Racing Course","Japan",5.807,18,2,"1:30.983","Lewis Hamilton","Figure-eight layout with the famous Esses and 130R. One of the most technically demanding circuits.",["F1","GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":180,"gear":4,"difficulty":"high","notes":"Entry sets up the S-curves. Crucial to nail."},
        {"number":3,"name":"S Curves","type":"fast","speed":200,"gear":5,"difficulty":"very high","notes":"Legendary flowing section. Flat in modern cars."},
        {"number":4,"name":"Dunlop","type":"fast","speed":220,"gear":5,"difficulty":"high","notes":"Fast left under the bridge. Commitment required."},
        {"number":5,"name":"Degner 1","type":"medium","speed":155,"gear":4,"difficulty":"high","notes":"Trail brake into this corner."},
        {"number":6,"name":"Degner 2","type":"medium","speed":120,"gear":3,"difficulty":"high","notes":"Tighter. Easy to lose rear."},
        {"number":7,"name":"Hairpin","type":"hairpin","speed":60,"gear":2,"difficulty":"medium","notes":"Slowest point. Good overtaking opportunity."},
        {"number":8,"name":"Spoon","type":"double apex","speed":165,"gear":4,"difficulty":"very high","notes":"Long double-apex left. Exit speed crucial."},
        {"number":9,"name":"130R","type":"fast","speed":305,"gear":7,"difficulty":"very high","notes":"One of the fastest corners. Flat or nothing."},
        {"number":10,"name":"Casio Triangle","type":"chicane","speed":85,"gear":2,"difficulty":"medium","notes":"Final chicane. Exit speed determines lap time."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":310,"target_speed":180,"brake_pressure":85,"downshift":"8-7-6-5-4"},
        {"corner":5,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":155,"brake_pressure":80,"downshift":"6-5-4"},
        {"corner":7,"marker":"100m","distance_m":95,"initial_speed":260,"target_speed":60,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":10,"marker":"125m","distance_m":115,"initial_speed":310,"target_speed":85,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"}
    ],["F1 25","ACC","iRacing"]),
    _track("imola","Autodromo Enzo e Dino Ferrari","Italy",4.909,19,1,"1:15.484","Lewis Hamilton","Historic circuit with elevation changes. Challenging and unforgiving layout.",["F1","GT3","GT4"],[
        {"number":1,"name":"Tamburello","type":"chicane","speed":130,"gear":3,"difficulty":"medium","notes":"Fast chicane. Good entry sets up the lap."},
        {"number":2,"name":"Villeneuve","type":"chicane","speed":85,"gear":2,"difficulty":"medium","notes":"Named after Gilles. Requires precision."},
        {"number":3,"name":"Tosa","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Uphill braking. Late apex for hill climb."},
        {"number":4,"name":"Piratella","type":"fast","speed":240,"gear":6,"difficulty":"high","notes":"Crest at entry. Trust car balance."},
        {"number":5,"name":"Acque Minerali","type":"chicane","speed":110,"gear":3,"difficulty":"high","notes":"Downhill chicane. Easy to overcook entry."},
        {"number":6,"name":"Variante Alta","type":"chicane","speed":95,"gear":3,"difficulty":"medium","notes":"Technical chicane. Sets up Rivazza."},
        {"number":7,"name":"Rivazza 1","type":"medium","speed":155,"gear":4,"difficulty":"high","notes":"Double left. Carry speed through."},
        {"number":8,"name":"Rivazza 2","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Exit onto main straight. Maximize speed."}
    ],[
        {"corner":1,"marker":"75m","distance_m":70,"initial_speed":300,"target_speed":130,"brake_pressure":85,"downshift":"7-6-5-4-3"},
        {"corner":2,"marker":"100m","distance_m":90,"initial_speed":290,"target_speed":85,"brake_pressure":95,"downshift":"7-6-5-4-3-2"},
        {"corner":3,"marker":"75m","distance_m":70,"initial_speed":260,"target_speed":95,"brake_pressure":90,"downshift":"6-5-4-3"},
        {"corner":5,"marker":"75m","distance_m":65,"initial_speed":280,"target_speed":110,"brake_pressure":90,"downshift":"7-6-5-4-3"},
        {"corner":7,"marker":"100m","distance_m":95,"initial_speed":285,"target_speed":155,"brake_pressure":85,"downshift":"7-6-5-4"}
    ],["F1 25","ACC"]),
    _track("barcelona","Circuit de Barcelona-Catalunya","Spain",4.675,16,2,"1:18.149","Max Verstappen","Technical circuit used for F1 testing. Variety of corner types.",["F1","GT3","GT4"],[
        {"number":1,"name":"Elf","type":"medium","speed":150,"gear":4,"difficulty":"medium","notes":"Good overtaking opportunity into Turn 1."},
        {"number":3,"name":"Turn 3","type":"fast","speed":195,"gear":5,"difficulty":"very high","notes":"Long fast right. Tests downforce and tires."},
        {"number":5,"name":"Seat Chicane","type":"chicane","speed":80,"gear":2,"difficulty":"medium","notes":"Sets up back straight."},
        {"number":9,"name":"Campsa","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Fast right over crest. Blind entry."},
        {"number":10,"name":"La Caixa","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Heavy braking zone."},
        {"number":16,"name":"New Chicane","type":"chicane","speed":115,"gear":3,"difficulty":"medium","notes":"Final chicane. Critical for lap time."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":300,"target_speed":150,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":5,"marker":"75m","distance_m":70,"initial_speed":250,"target_speed":80,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":10,"marker":"100m","distance_m":90,"initial_speed":280,"target_speed":90,"brake_pressure":95,"downshift":"7-6-5-4-3"}
    ],["F1 25","ACC"]),
    _track("zandvoort","Circuit Zandvoort","Netherlands",4.259,14,2,"1:11.097","Lewis Hamilton","High-speed with unique banked corners. Dramatic elevation and the famous Tarzan hairpin.",["F1","GT3","GT4"],[
        {"number":1,"name":"Tarzan","type":"hairpin","speed":70,"gear":2,"difficulty":"medium","notes":"Famous hairpin. Good overtaking spot."},
        {"number":3,"name":"Hugenholtz","type":"medium","speed":185,"gear":5,"difficulty":"high","notes":"Banked entry. Use the banking."},
        {"number":7,"name":"Scheivlak","type":"fast","speed":230,"gear":6,"difficulty":"very high","notes":"Blind, fast left. Requires commitment."},
        {"number":13,"name":"Arie Luyendyk","type":"banked","speed":280,"gear":7,"difficulty":"high","notes":"18-degree banking. Unique in F1."},
        {"number":14,"name":"Final Turn","type":"banked","speed":270,"gear":7,"difficulty":"high","notes":"Banked final. Flat if brave enough."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":290,"target_speed":70,"brake_pressure":100,"downshift":"7-6-5-4-3-2"},
        {"corner":7,"marker":"50m","distance_m":45,"initial_speed":255,"target_speed":230,"brake_pressure":40,"downshift":"6"}
    ],["F1 25","ACC"]),
    _track("nurburgring_gp","Nürburgring GP-Strecke","Germany",5.148,15,2,"1:29.468","Michael Schumacher","Modern GP circuit adjacent to the Nordschleife. Technical with good overtaking.",["F1","GT3","GT4"],[
        {"number":1,"name":"Yokohama-S","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Entry to the track. Trail braking essential."},
        {"number":2,"name":"Mercedes Arena","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Best overtaking spot."},
        {"number":5,"name":"Veedol Chicane","type":"chicane","speed":70,"gear":2,"difficulty":"medium","notes":"Tight chicane. Curb usage important."},
        {"number":6,"name":"Dunlop Hairpin","type":"hairpin","speed":65,"gear":2,"difficulty":"low","notes":"Focus on exit traction."},
        {"number":7,"name":"Coca-Cola Kurve","type":"fast","speed":225,"gear":5,"difficulty":"high","notes":"Long sweeping right. Builds confidence."}
    ],[
        {"corner":2,"marker":"100m","distance_m":95,"initial_speed":230,"target_speed":80,"brake_pressure":95,"downshift":"5-4-3-2"},
        {"corner":5,"marker":"100m","distance_m":90,"initial_speed":260,"target_speed":70,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":6,"marker":"75m","distance_m":70,"initial_speed":220,"target_speed":65,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["F1 25","ACC","iRacing"]),
    _track("singapore","Marina Bay Street Circuit","Singapore",4.940,19,3,"1:35.867","Lewis Hamilton","Night race on a demanding street circuit. High heat and humidity add to the challenge.",["F1"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":105,"gear":3,"difficulty":"medium","notes":"Heavy braking into first left."},
        {"number":5,"name":"Turn 5","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Tight left-hander."},
        {"number":7,"name":"Turn 7","type":"slow","speed":70,"gear":2,"difficulty":"high","notes":"Very tight. Walls close."},
        {"number":14,"name":"Turn 14","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Anderson Bridge."},
        {"number":18,"name":"Turn 18","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Second to last. Exit speed matters."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":300,"target_speed":105,"brake_pressure":90,"downshift":"7-6-5-4-3"},
        {"corner":7,"marker":"75m","distance_m":65,"initial_speed":200,"target_speed":70,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["F1 25"]),
    _track("laguna_seca","WeatherTech Raceway Laguna Seca","USA",3.602,11,0,"1:05.786","Various","Home of the legendary Corkscrew. Dramatic elevation changes and a challenging layout.",["GT3","GT4"],[
        {"number":1,"name":"Andretti Hairpin","type":"hairpin","speed":60,"gear":2,"difficulty":"medium","notes":"Tight hairpin. Focus on late apex."},
        {"number":2,"name":"Turn 2","type":"fast","speed":195,"gear":5,"difficulty":"high","notes":"Fast uphill left."},
        {"number":5,"name":"Turn 5","type":"medium","speed":130,"gear":3,"difficulty":"medium","notes":"Downhill entry. Trail brake carefully."},
        {"number":6,"name":"Turn 6","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Setup for the Corkscrew."},
        {"number":8,"name":"The Corkscrew","type":"slow","speed":65,"gear":2,"difficulty":"very high","notes":"Legendary blind, downhill, left-right. Iconic."},
        {"number":9,"name":"Rainey Curve","type":"medium","speed":140,"gear":4,"difficulty":"high","notes":"Fast left after Corkscrew."},
        {"number":11,"name":"Turn 11","type":"medium","speed":120,"gear":3,"difficulty":"medium","notes":"Final corner. Exit speed crucial."}
    ],[
        {"corner":1,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":60,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":6,"marker":"75m","distance_m":65,"initial_speed":200,"target_speed":85,"brake_pressure":85,"downshift":"5-4-3-2"},
        {"corner":8,"marker":"50m","distance_m":40,"initial_speed":130,"target_speed":65,"brake_pressure":90,"downshift":"3-2"}
    ],["ACC","iRacing"]),
    _track("bathurst","Mount Panorama Circuit","Australia",6.213,23,0,"2:01.505","Various","The Mountain. One of the most dramatic and dangerous circuits with extreme elevation changes.",["GT3","GT4"],[
        {"number":1,"name":"Hell Corner","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Right-hander onto Mountain Straight."},
        {"number":2,"name":"Mountain Straight","type":"straight","speed":270,"gear":7,"difficulty":"low","notes":"Full throttle uphill."},
        {"number":3,"name":"The Cutting","type":"slow","speed":65,"gear":2,"difficulty":"high","notes":"Sharp left. Walls very close."},
        {"number":6,"name":"The Dipper","type":"fast","speed":180,"gear":4,"difficulty":"very high","notes":"Fast, blind, downhill. Maximum commitment."},
        {"number":11,"name":"Forrest Elbow","type":"slow","speed":70,"gear":2,"difficulty":"high","notes":"Tight left at the top. Walls everywhere."},
        {"number":15,"name":"The Chase","type":"fast","speed":230,"gear":6,"difficulty":"very high","notes":"High-speed through the valley. Flat out."},
        {"number":23,"name":"Murray Corner","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Final corner. Exit speed critical for lap time."}
    ],[
        {"corner":1,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":80,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":3,"marker":"100m","distance_m":85,"initial_speed":270,"target_speed":65,"brake_pressure":100,"downshift":"7-6-5-4-3-2"},
        {"corner":23,"marker":"75m","distance_m":65,"initial_speed":230,"target_speed":75,"brake_pressure":95,"downshift":"6-5-4-3-2"}
    ],["ACC","iRacing"]),
    _track("brands_hatch","Brands Hatch GP","United Kingdom",3.908,9,0,"1:21.000","Various","Dramatic British circuit with steep elevation. The amphitheatre at Paddock Hill is legendary.",["GT3","GT4"],[
        {"number":1,"name":"Paddock Hill Bend","type":"fast","speed":190,"gear":5,"difficulty":"very high","notes":"Blind downhill right. One of the scariest entries in racing."},
        {"number":2,"name":"Druids","type":"hairpin","speed":60,"gear":2,"difficulty":"medium","notes":"Tight hairpin at the top."},
        {"number":4,"name":"Surtees","type":"fast","speed":200,"gear":5,"difficulty":"high","notes":"Fast downhill left."},
        {"number":6,"name":"Hawthorn","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Fast right leading to Westfield."},
        {"number":9,"name":"Clark Curve","type":"fast","speed":220,"gear":5,"difficulty":"high","notes":"Final corner. Full throttle onto main straight."}
    ],[
        {"corner":2,"marker":"75m","distance_m":65,"initial_speed":220,"target_speed":60,"brake_pressure":95,"downshift":"5-4-3-2"},
        {"corner":4,"marker":"50m","distance_m":40,"initial_speed":200,"target_speed":200,"brake_pressure":20,"downshift":""}
    ],["ACC"]),
    _track("kyalami","Kyalami Grand Prix Circuit","South Africa",4.522,16,2,"1:28.000","Various","South African classic. Fast and flowing with a mix of high and low-speed corners.",["GT3","GT4"],[
        {"number":1,"name":"The Kink","type":"fast","speed":250,"gear":6,"difficulty":"high","notes":"Fast left entry. Sets the tone."},
        {"number":3,"name":"Crowthorne","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Tight right-hander."},
        {"number":5,"name":"Jukskei Sweep","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Long fast right. Confidence builder."},
        {"number":12,"name":"Cheetah","type":"fast","speed":220,"gear":5,"difficulty":"high","notes":"Fast left. Flat or slight lift."},
        {"number":16,"name":"Sunset","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Final corner. Exit speed important."}
    ],[
        {"corner":3,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":85,"brake_pressure":95,"downshift":"6-5-4-3-2"}
    ],["ACC"]),
    _track("misano","Misano World Circuit","Italy",4.226,16,2,"1:33.000","Various","Technical Italian circuit with a mix of slow and medium-speed corners.",["GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Heavy braking from main straight."},
        {"number":4,"name":"Turn 4","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Tight hairpin."},
        {"number":8,"name":"Turn 8","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Medium speed right."},
        {"number":14,"name":"Quercia","type":"fast","speed":200,"gear":5,"difficulty":"high","notes":"Fast right. Flat or slight lift."},
        {"number":16,"name":"Turn 16","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Final corner. Exit speed crucial."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":280,"target_speed":95,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":4,"marker":"75m","distance_m":65,"initial_speed":200,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["ACC"]),
    _track("hungaroring","Hungaroring","Hungary",4.381,14,2,"1:16.627","Lewis Hamilton","Tight, twisty circuit often compared to a large kart track. Overtaking is difficult.",["F1","GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Downhill braking. Good overtaking spot."},
        {"number":2,"name":"Turn 2","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Fast right leading into technical section."},
        {"number":4,"name":"Turn 4","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Tight hairpin. Late apex important."},
        {"number":6,"name":"Turn 6","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Another hairpin. Patience needed."},
        {"number":11,"name":"Turn 11","type":"fast","speed":220,"gear":5,"difficulty":"high","notes":"Fastest corner. Flat with downforce."},
        {"number":14,"name":"Turn 14","type":"slow","speed":105,"gear":3,"difficulty":"medium","notes":"Final corner. Exit speed onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":310,"target_speed":145,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":4,"marker":"75m","distance_m":65,"initial_speed":220,"target_speed":85,"brake_pressure":90,"downshift":"5-4-3-2"},
        {"corner":6,"marker":"75m","distance_m":60,"initial_speed":180,"target_speed":80,"brake_pressure":85,"downshift":"4-3-2"}
    ],["F1 25","ACC"]),
    _track("watkins_glen","Watkins Glen International","USA",5.430,11,0,"1:28.000","Various","Classic American road course. Fast and flowing with dramatic elevation changes.",["GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"fast","speed":235,"gear":6,"difficulty":"high","notes":"Fast right-hander. Commitment needed."},
        {"number":2,"name":"The Esses","type":"fast","speed":200,"gear":5,"difficulty":"very high","notes":"Quick direction changes. Rhythm is key."},
        {"number":5,"name":"Inner Loop","type":"chicane","speed":70,"gear":2,"difficulty":"medium","notes":"Tight chicane. Good overtaking spot."},
        {"number":7,"name":"Toe of the Boot","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Setup for The Boot."},
        {"number":8,"name":"The Boot","type":"medium","speed":150,"gear":4,"difficulty":"high","notes":"Long uphill section through the extension."},
        {"number":11,"name":"Turn 11","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Final corner. Full throttle exit."}
    ],[
        {"corner":5,"marker":"100m","distance_m":85,"initial_speed":270,"target_speed":70,"brake_pressure":100,"downshift":"7-6-5-4-3-2"},
        {"corner":7,"marker":"75m","distance_m":60,"initial_speed":200,"target_speed":80,"brake_pressure":85,"downshift":"5-4-3-2"}
    ],["iRacing","ACC"]),
    _track("cota","Circuit of the Americas","USA",5.513,20,2,"1:36.169","Charles Leclerc","Modern US circuit inspired by great tracks. Features Turn 1 hill climb and flowing Esses.",["F1","GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":105,"gear":3,"difficulty":"high","notes":"Uphill blind braking zone. Dramatic."},
        {"number":3,"name":"Esses","type":"fast","speed":240,"gear":6,"difficulty":"very high","notes":"Maggots-Becketts inspired. Flat through."},
        {"number":11,"name":"Turn 11","type":"hairpin","speed":65,"gear":2,"difficulty":"medium","notes":"Hairpin. Good overtaking spot."},
        {"number":12,"name":"Turn 12","type":"slow","speed":100,"gear":3,"difficulty":"medium","notes":"DRS detection zone."},
        {"number":15,"name":"Turn 15","type":"medium","speed":165,"gear":4,"difficulty":"high","notes":"Fast left. Tests rear stability."},
        {"number":19,"name":"Turn 19","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Penultimate. Exit speed matters."},
        {"number":20,"name":"Turn 20","type":"medium","speed":135,"gear":3,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":310,"target_speed":105,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":11,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":65,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":12,"marker":"50m","distance_m":40,"initial_speed":175,"target_speed":100,"brake_pressure":75,"downshift":"4-3"}
    ],["F1 25","iRacing"]),
    _track("interlagos","Autódromo José Carlos Pace","Brazil",4.309,15,2,"1:10.540","Valtteri Bottas","Counter-clockwise Brazilian classic. Steep elevation and passionate fans.",["F1"],[
        {"number":1,"name":"Senna S","type":"chicane","speed":110,"gear":3,"difficulty":"high","notes":"Named after Ayrton. Critical entry to the lap."},
        {"number":4,"name":"Descida do Lago","type":"fast","speed":255,"gear":6,"difficulty":"high","notes":"Fast downhill left."},
        {"number":6,"name":"Ferradura","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Horseshoe corner. Good flow needed."},
        {"number":8,"name":"Laranjinha","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Slow right. Exit speed matters."},
        {"number":10,"name":"Mergulho","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Fast downhill. Flat in qualifying."},
        {"number":12,"name":"Junção","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Tight right onto back straight."},
        {"number":15,"name":"Subida dos Boxes","type":"medium","speed":140,"gear":4,"difficulty":"medium","notes":"Uphill entry. Leads onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":310,"target_speed":110,"brake_pressure":90,"downshift":"7-6-5-4-3"},
        {"corner":8,"marker":"75m","distance_m":60,"initial_speed":220,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"},
        {"corner":12,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":85,"brake_pressure":95,"downshift":"6-5-4-3-2"}
    ],["F1 25"]),
    # Additional F1 25 tracks
    _track("jeddah","Jeddah Corniche Circuit","Saudi Arabia",6.174,27,3,"1:30.734","Lewis Hamilton","The fastest street circuit. Narrow, high-speed walls with minimal run-off.",["F1"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Sharp right to start. Trail brake in."},
        {"number":4,"name":"Turn 4","type":"fast","speed":240,"gear":6,"difficulty":"high","notes":"Fast blind left. Commitment required."},
        {"number":13,"name":"Turn 13","type":"slow","speed":85,"gear":2,"difficulty":"high","notes":"Tight right between walls."},
        {"number":22,"name":"Turn 22","type":"fast","speed":250,"gear":6,"difficulty":"very high","notes":"Fast kink between the walls."},
        {"number":27,"name":"Turn 27","type":"medium","speed":155,"gear":4,"difficulty":"high","notes":"Final corner. Exit speed crucial."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":290,"target_speed":165,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":13,"marker":"75m","distance_m":65,"initial_speed":230,"target_speed":85,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":27,"marker":"75m","distance_m":60,"initial_speed":260,"target_speed":155,"brake_pressure":80,"downshift":"6-5-4"}
    ],["F1 25"]),
    _track("melbourne","Albert Park Circuit","Australia",5.278,14,2,"1:20.235","Charles Leclerc","Semi-permanent street circuit around a lake. Fast sweepers and tight chicanes.",["F1"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"First braking zone. Good overtaking."},
        {"number":3,"name":"Turn 3","type":"fast","speed":230,"gear":5,"difficulty":"high","notes":"Fast right sweeper."},
        {"number":6,"name":"Turn 6","type":"chicane","speed":80,"gear":2,"difficulty":"medium","notes":"Tight chicane. Good exit needed."},
        {"number":9,"name":"Turn 9","type":"fast","speed":255,"gear":6,"difficulty":"high","notes":"High-speed approach to lakeside."},
        {"number":11,"name":"Turn 11","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Braking zone for chicane."},
        {"number":13,"name":"Turn 13","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Fast right. Leads to final turn."},
        {"number":14,"name":"Turn 14","type":"slow","speed":105,"gear":3,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":300,"target_speed":145,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":6,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":80,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":11,"marker":"75m","distance_m":65,"initial_speed":260,"target_speed":90,"brake_pressure":90,"downshift":"6-5-4-3"}
    ],["F1 25"]),
    _track("shanghai","Shanghai International Circuit","China",5.451,16,2,"1:32.238","Michael Schumacher","Designed by Hermann Tilke with unique characteristics. Features the enormous Turn 1-2-3 complex.",["F1"],[
        {"number":1,"name":"Turn 1-2-3","type":"double apex","speed":120,"gear":3,"difficulty":"very high","notes":"Enormous decreasing radius. Key to lap time."},
        {"number":6,"name":"Turn 6","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Hairpin. Good overtaking spot."},
        {"number":8,"name":"Turn 8","type":"fast","speed":220,"gear":5,"difficulty":"high","notes":"Fast right-hander. Tests downforce."},
        {"number":11,"name":"Turn 11","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Another hairpin. Exit speed important."},
        {"number":13,"name":"Turn 13","type":"fast","speed":245,"gear":6,"difficulty":"high","notes":"Fast entry to back straight."},
        {"number":14,"name":"Turn 14","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Setup for final sector."},
        {"number":16,"name":"Turn 16","type":"medium","speed":140,"gear":4,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":310,"target_speed":120,"brake_pressure":90,"downshift":"7-6-5-4-3"},
        {"corner":6,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":85,"brake_pressure":95,"downshift":"6-5-4-3-2"},
        {"corner":11,"marker":"75m","distance_m":60,"initial_speed":220,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"},
        {"corner":14,"marker":"75m","distance_m":60,"initial_speed":280,"target_speed":165,"brake_pressure":80,"downshift":"7-6-5-4"}
    ],["F1 25"]),
    _track("miami","Miami International Autodrome","USA",5.412,19,3,"1:29.708","Max Verstappen","Street circuit around Hard Rock Stadium. Mix of high-speed sections and tight corners.",["F1"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Braking from main straight."},
        {"number":4,"name":"Turn 4","type":"chicane","speed":95,"gear":3,"difficulty":"medium","notes":"Chicane before back straight."},
        {"number":7,"name":"Turn 7","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Hairpin at the end of back straight."},
        {"number":11,"name":"Turn 11","type":"medium","speed":175,"gear":4,"difficulty":"high","notes":"Fast left through stadium section."},
        {"number":17,"name":"Turn 17","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Tight right leading to final sector."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":310,"target_speed":155,"brake_pressure":85,"downshift":"7-6-5-4"},
        {"corner":7,"marker":"100m","distance_m":90,"initial_speed":290,"target_speed":85,"brake_pressure":95,"downshift":"7-6-5-4-3-2"},
        {"corner":17,"marker":"75m","distance_m":60,"initial_speed":220,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["F1 25"]),
    _track("montreal","Circuit Gilles-Villeneuve","Canada",4.361,14,2,"1:13.078","Valtteri Bottas","The home of Canadian GP on Île Notre-Dame. Wall of Champions at the final chicane.",["F1"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Wide entry. Multiple lines possible."},
        {"number":3,"name":"Turn 3","type":"chicane","speed":80,"gear":2,"difficulty":"medium","notes":"First chicane. Curb usage matters."},
        {"number":6,"name":"Turn 6","type":"chicane","speed":120,"gear":3,"difficulty":"high","notes":"Fast chicane. Commitment needed."},
        {"number":8,"name":"Turn 8","type":"chicane","speed":90,"gear":2,"difficulty":"medium","notes":"Chicane leading to hairpin."},
        {"number":10,"name":"Turn 10 (Hairpin)","type":"hairpin","speed":60,"gear":2,"difficulty":"medium","notes":"Slowest point. Focus on exit traction."},
        {"number":13,"name":"Turn 13 (Chicane)","type":"chicane","speed":110,"gear":3,"difficulty":"very high","notes":"Wall of Champions! Legendary exit."},
        {"number":14,"name":"Turn 14","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":90,"initial_speed":300,"target_speed":95,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":10,"marker":"75m","distance_m":70,"initial_speed":250,"target_speed":60,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":13,"marker":"75m","distance_m":60,"initial_speed":280,"target_speed":110,"brake_pressure":90,"downshift":"7-6-5-4-3"}
    ],["F1 25"]),
    _track("yas_marina","Yas Marina Circuit","Abu Dhabi",5.281,16,2,"1:26.103","Max Verstappen","Season finale venue. Unique hotel straddling the track and spectacular night lighting.",["F1"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Hard braking from main straight."},
        {"number":5,"name":"Turn 5","type":"chicane","speed":85,"gear":2,"difficulty":"medium","notes":"Tight chicane around the hotel."},
        {"number":7,"name":"Turn 7","type":"medium","speed":175,"gear":5,"difficulty":"high","notes":"Fast right-hander."},
        {"number":9,"name":"Turn 9","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Hairpin. Good overtaking zone."},
        {"number":14,"name":"Turn 14","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Left-hander in final sector."},
        {"number":16,"name":"Turn 16","type":"medium","speed":150,"gear":4,"difficulty":"medium","notes":"Final corner. Exit speed matters."}
    ],[
        {"corner":1,"marker":"100m","distance_m":95,"initial_speed":325,"target_speed":95,"brake_pressure":100,"downshift":"8-7-6-5-4-3"},
        {"corner":5,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":85,"brake_pressure":90,"downshift":"6-5-4-3-2"},
        {"corner":9,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":80,"brake_pressure":95,"downshift":"6-5-4-3-2"}
    ],["F1 25"]),
    _track("lusail","Lusail International Circuit","Qatar",5.419,16,2,"1:24.319","Max Verstappen","Desert circuit with long straights and high-speed corners. Night race under floodlights.",["F1"],[
        {"number":1,"name":"Turn 1","type":"medium","speed":180,"gear":5,"difficulty":"high","notes":"Fast right-hander. Sets up the lap."},
        {"number":4,"name":"Turn 4","type":"fast","speed":250,"gear":6,"difficulty":"high","notes":"High-speed left. Flat in F1."},
        {"number":6,"name":"Turn 6","type":"medium","speed":170,"gear":4,"difficulty":"medium","notes":"Medium right. Tests balance."},
        {"number":10,"name":"Turn 10","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Braking zone for tight section."},
        {"number":12,"name":"Turn 12","type":"fast","speed":240,"gear":6,"difficulty":"high","notes":"Fast left towards back straight."},
        {"number":16,"name":"Turn 16","type":"medium","speed":155,"gear":4,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"75m","distance_m":65,"initial_speed":320,"target_speed":180,"brake_pressure":80,"downshift":"8-7-6-5"},
        {"corner":10,"marker":"100m","distance_m":85,"initial_speed":280,"target_speed":90,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":16,"marker":"75m","distance_m":60,"initial_speed":260,"target_speed":155,"brake_pressure":80,"downshift":"6-5-4"}
    ],["F1 25"]),
    _track("las_vegas","Las Vegas Strip Circuit","USA",6.201,17,2,"1:35.490","Oscar Piastri","Night race on the iconic Las Vegas Strip. Long straights and high-speed corners.",["F1"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Braking from 340 km/h on the Strip."},
        {"number":5,"name":"Turn 5","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Medium right through the resort area."},
        {"number":11,"name":"Turn 11","type":"fast","speed":245,"gear":6,"difficulty":"high","notes":"Fast sweeper along the highway."},
        {"number":14,"name":"Turn 14","type":"chicane","speed":100,"gear":3,"difficulty":"medium","notes":"Chicane before final straight."},
        {"number":17,"name":"Turn 17","type":"medium","speed":140,"gear":4,"difficulty":"medium","notes":"Final corner back onto the Strip."}
    ],[
        {"corner":1,"marker":"125m","distance_m":110,"initial_speed":340,"target_speed":95,"brake_pressure":100,"downshift":"8-7-6-5-4-3"},
        {"corner":14,"marker":"75m","distance_m":60,"initial_speed":260,"target_speed":100,"brake_pressure":90,"downshift":"6-5-4-3"}
    ],["F1 25"]),
    _track("baku","Baku City Circuit","Azerbaijan",6.003,20,2,"1:43.009","Charles Leclerc","Street circuit around the old city. Mix of tight old town and 2.2 km straight.",["F1"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":95,"gear":3,"difficulty":"medium","notes":"Braking from main straight."},
        {"number":3,"name":"Turn 3","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Tight right in old town."},
        {"number":8,"name":"Castle Section","type":"slow","speed":60,"gear":2,"difficulty":"very high","notes":"Extremely tight. Walls inches away."},
        {"number":15,"name":"Turn 15","type":"medium","speed":165,"gear":4,"difficulty":"medium","notes":"Opens up to the harbor section."},
        {"number":16,"name":"Turn 16","type":"fast","speed":290,"gear":7,"difficulty":"high","notes":"Flat out alongside the sea."},
        {"number":20,"name":"Turn 20","type":"slow","speed":80,"gear":2,"difficulty":"high","notes":"Hard braking after 2.2km straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":300,"target_speed":95,"brake_pressure":95,"downshift":"7-6-5-4-3"},
        {"corner":8,"marker":"50m","distance_m":40,"initial_speed":150,"target_speed":60,"brake_pressure":90,"downshift":"3-2"},
        {"corner":20,"marker":"125m","distance_m":110,"initial_speed":340,"target_speed":80,"brake_pressure":100,"downshift":"8-7-6-5-4-3-2"}
    ],["F1 25"]),
    # Additional ACC/iRacing tracks
    _track("paul_ricard","Paul Ricard Circuit","France",5.842,15,2,"1:32.740","Sebastian Vettel","Technical circuit with massive run-off areas. Blue and red painted tarmac is iconic.",["GT3","GT4"],[
        {"number":1,"name":"Verrerie","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Medium right after start."},
        {"number":5,"name":"Sainte Baume","type":"fast","speed":230,"gear":5,"difficulty":"high","notes":"Fast section through painted run-off."},
        {"number":8,"name":"Beausset","type":"fast","speed":240,"gear":6,"difficulty":"high","notes":"Fast double-right. Tests commitment."},
        {"number":11,"name":"Signes","type":"fast","speed":280,"gear":7,"difficulty":"very high","notes":"One of the fastest corners. Nearly flat."},
        {"number":15,"name":"Bendor","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Tight right before main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":290,"target_speed":160,"brake_pressure":80,"downshift":"7-6-5-4"},
        {"corner":15,"marker":"75m","distance_m":65,"initial_speed":240,"target_speed":90,"brake_pressure":95,"downshift":"6-5-4-3"}
    ],["ACC"]),
    _track("indianapolis","Indianapolis Motor Speedway (Road)","USA",4.167,14,0,"1:10.000","Various","The legendary Brickyard. Road course combines infield with part of the iconic oval.",["GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Sharp right into the infield."},
        {"number":4,"name":"Turn 4","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Fast right leading to oval section."},
        {"number":7,"name":"Turn 7","type":"fast","speed":230,"gear":6,"difficulty":"high","notes":"Rejoining the oval banking."},
        {"number":12,"name":"Turn 12","type":"slow","speed":75,"gear":2,"difficulty":"medium","notes":"Tight hairpin in the infield."},
        {"number":14,"name":"Turn 14","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Final corner onto the main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":280,"target_speed":85,"brake_pressure":95,"downshift":"7-6-5-4-3-2"},
        {"corner":12,"marker":"75m","distance_m":60,"initial_speed":210,"target_speed":75,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["ACC","iRacing"]),
    _track("donington","Donington Park GP","United Kingdom",4.020,12,0,"1:25.000","Various","Classic British circuit with dramatic elevation. Home of the legendary 1993 Senna drive.",["GT3","GT4"],[
        {"number":1,"name":"Redgate","type":"medium","speed":140,"gear":4,"difficulty":"medium","notes":"Downhill entry. Trail brake carefully."},
        {"number":2,"name":"Craner Curves","type":"fast","speed":230,"gear":6,"difficulty":"very high","notes":"Fast downhill esses. Commitment required."},
        {"number":3,"name":"Old Hairpin","type":"hairpin","speed":55,"gear":2,"difficulty":"medium","notes":"Tight hairpin at bottom of the hill."},
        {"number":5,"name":"McLeans","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Fast left over crest. Blind entry."},
        {"number":8,"name":"Melbourne Hairpin","type":"hairpin","speed":50,"gear":1,"difficulty":"medium","notes":"Slowest point. Focus on exit."},
        {"number":12,"name":"Goddards","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Final corner. Exit speed matters."}
    ],[
        {"corner":1,"marker":"75m","distance_m":65,"initial_speed":250,"target_speed":140,"brake_pressure":80,"downshift":"6-5-4"},
        {"corner":3,"marker":"75m","distance_m":65,"initial_speed":230,"target_speed":55,"brake_pressure":100,"downshift":"6-5-4-3-2"},
        {"corner":8,"marker":"100m","distance_m":85,"initial_speed":230,"target_speed":50,"brake_pressure":100,"downshift":"5-4-3-2-1"}
    ],["ACC"]),
    _track("valencia","Circuit Ricardo Tormo","Spain",4.005,14,0,"1:30.000","Various","Technical Spanish circuit in Valencia. Used for MotoGP and GT racing.",["GT3","GT4"],[
        {"number":1,"name":"Turn 1","type":"slow","speed":90,"gear":3,"difficulty":"medium","notes":"Heavy braking from start straight."},
        {"number":4,"name":"Turn 4","type":"fast","speed":200,"gear":5,"difficulty":"high","notes":"Fast left. Leads to back straight."},
        {"number":8,"name":"Turn 8","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Tight hairpin."},
        {"number":11,"name":"Turn 11","type":"fast","speed":210,"gear":5,"difficulty":"high","notes":"Fast right sweeper."},
        {"number":14,"name":"Turn 14","type":"medium","speed":130,"gear":3,"difficulty":"medium","notes":"Final corner onto main straight."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":270,"target_speed":90,"brake_pressure":95,"downshift":"6-5-4-3"},
        {"corner":8,"marker":"75m","distance_m":60,"initial_speed":220,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["ACC"]),
    _track("oulton_park","Oulton Park International","United Kingdom",4.307,17,0,"1:32.000","Various","Flowing British circuit through beautiful parkland. Elevation changes and tricky blind corners.",["GT3","GT4"],[
        {"number":1,"name":"Old Hall","type":"fast","speed":200,"gear":5,"difficulty":"high","notes":"Fast downhill right. Blind entry."},
        {"number":4,"name":"Cascades","type":"fast","speed":185,"gear":5,"difficulty":"very high","notes":"Fast downhill double-apex. Spectacular."},
        {"number":8,"name":"Knickerbrook","type":"fast","speed":190,"gear":5,"difficulty":"high","notes":"Fast chicane. Rhythm needed."},
        {"number":12,"name":"Druids","type":"hairpin","speed":55,"gear":2,"difficulty":"medium","notes":"Tight hairpin. Late apex."},
        {"number":17,"name":"Deer Leap","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Final corner. Exit for main straight."}
    ],[
        {"corner":12,"marker":"75m","distance_m":60,"initial_speed":200,"target_speed":55,"brake_pressure":100,"downshift":"5-4-3-2"}
    ],["ACC"]),
    _track("snetterton","Snetterton 300","United Kingdom",4.779,12,0,"1:47.000","Various","Fast Norfolk circuit. Long straights punctuated by technical infield sections.",["GT3","GT4"],[
        {"number":1,"name":"Riches","type":"medium","speed":160,"gear":4,"difficulty":"medium","notes":"Medium right after back straight."},
        {"number":3,"name":"Montreal","type":"medium","speed":145,"gear":4,"difficulty":"medium","notes":"Named after the Canadian chicane it resembles."},
        {"number":5,"name":"Agostini","type":"slow","speed":80,"gear":2,"difficulty":"medium","notes":"Tight right-hander."},
        {"number":9,"name":"Coram","type":"fast","speed":220,"gear":6,"difficulty":"high","notes":"Fast double-apex. Carry speed through."},
        {"number":12,"name":"Murrays","type":"slow","speed":85,"gear":2,"difficulty":"medium","notes":"Final corner complex."}
    ],[
        {"corner":1,"marker":"100m","distance_m":85,"initial_speed":280,"target_speed":160,"brake_pressure":80,"downshift":"7-6-5-4"},
        {"corner":5,"marker":"75m","distance_m":60,"initial_speed":210,"target_speed":80,"brake_pressure":90,"downshift":"5-4-3-2"}
    ],["ACC"]),
]
