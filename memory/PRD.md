# Apex Academy - Motorsport Education Platform

## Original Problem Statement
Comprehensive motorsport website for F1/GT3/GT4 education, analysis, and fan content.

## Architecture
- Frontend: React 19 + Tailwind CSS + Framer Motion + Recharts
- Backend: FastAPI + MongoDB + Motor
- Auth: Emergent Google OAuth
- Payments: Stripe via emergentintegrations ($9.99/mo)
- Theme: Dark neon racing

## What's Implemented (April 2026)
- [x] 35 cars: 10 F1 (all F1 25 teams), 14 GT3 (ACC/iRacing), 11 GT4 (ACC)
- [x] 36 tracks: All F1 25 calendar + ACC + iRacing circuits
- [x] Engineer Mode: Interactive car setup with aero/suspension/tires/diff sliders + performance analysis
- [x] Trajectory Simulator: Draw racing lines on track maps (Monza, Spa) with scoring
- [x] Enhanced Telemetry: 5-tab analysis (Combined, Speed, Throttle/Brake, Gear/RPM, G-Forces)
- [x] Track guides with detailed corner analysis, braking points, downshift patterns, driver notes
- [x] Quiz system (4 quizzes, 4 categories)
- [x] Racing glossary with 20 terms
- [x] Motorsport news feed (mock data)
- [x] Community comments (auth-gated)
- [x] Google OAuth + Stripe subscription
- [x] Responsive dark theme with neon accents

## Backlog
### P0
- [ ] More trajectory simulator tracks
- [ ] Setup save/load to user profile

### P1  
- [ ] "Create the Perfect Lap" game
- [ ] Lap time comparison tool
- [ ] Real RSS feed integration
- [ ] AI driving assistant

### P2
- [ ] Setup sharing marketplace
- [ ] Mobile touch support for simulator
- [ ] Video integration for onboard footage
