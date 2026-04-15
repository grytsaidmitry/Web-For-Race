# Test Credentials for Apex Academy

## Google OAuth
- Authentication is via Google OAuth (Emergent-managed)
- No password-based credentials for OAuth flows
- Test accounts can be created via MongoDB seeding

## Test User Seeding
To create a test user with premium access:
```bash
mongosh --eval "
use('test_database');
var userId = 'test-user-' + Date.now();
var sessionToken = 'test_session_' + Date.now();
db.users.insertOne({
  user_id: userId,
  email: 'test@example.com',
  name: 'Test User',
  picture: 'https://via.placeholder.com/150',
  subscription_tier: 'premium',
  subscription_expires: new Date(Date.now() + 30*24*60*60*1000),
  created_at: new Date()
});
db.user_sessions.insertOne({
  user_id: userId,
  session_token: sessionToken,
  expires_at: new Date(Date.now() + 7*24*60*60*1000),
  created_at: new Date()
});
print('Session token: ' + sessionToken);
print('User ID: ' + userId);
"
```

## Stripe
- Test key: sk_test_emergent (already in .env)
- Subscription price: $9.99/month

## API Endpoints (Public)
- GET /api/tracks - List all tracks
- GET /api/cars - List all cars
- GET /api/quizzes - List quizzes
- GET /api/glossary - Racing glossary
- GET /api/news - Motorsport news

## API Endpoints (Auth Required)
- GET /api/auth/me - Current user
- POST /api/comments - Create comment
- GET /api/user/progress - User progress
