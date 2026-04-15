#!/usr/bin/env python3
"""
Comprehensive backend API testing for Apex Academy motorsports platform.
Tests all endpoints for correct data structure and expected counts.
"""

import requests
import sys
from datetime import datetime
import json

class ApexAcademyAPITester:
    def __init__(self, base_url="https://apex-academy-3.preview.emergentagent.com/api"):
        self.base_url = base_url
        self.session_token = None
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def log_result(self, test_name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {test_name}")
        else:
            print(f"❌ {test_name} - {details}")
            self.failed_tests.append(f"{test_name}: {details}")

    def test_api_root(self):
        """Test API root endpoint"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                expected_cars = 35  # 10 F1 + 14 GT3 + 11 GT4
                expected_tracks = 36
                
                success = (
                    data.get("message") == "Apex Academy API" and
                    data.get("cars") == expected_cars and
                    data.get("tracks") == expected_tracks
                )
                self.log_result("API Root", success, 
                    f"Expected cars: {expected_cars}, got: {data.get('cars')}. Expected tracks: {expected_tracks}, got: {data.get('tracks')}")
            else:
                self.log_result("API Root", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("API Root", False, str(e))

    def test_tracks_endpoint(self):
        """Test tracks endpoint - should return 36 tracks"""
        try:
            response = requests.get(f"{self.base_url}/tracks", timeout=10)
            if response.status_code == 200:
                tracks = response.json()
                success = len(tracks) == 36
                self.log_result("GET /tracks", success, f"Expected 36 tracks, got {len(tracks)}")
                
                # Test track structure
                if tracks:
                    track = tracks[0]
                    required_fields = ['track_id', 'name', 'country', 'length_km', 'turns', 'corners', 'braking_points']
                    missing_fields = [field for field in required_fields if field not in track]
                    self.log_result("Track Data Structure", len(missing_fields) == 0, 
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /tracks", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /tracks", False, str(e))

    def test_track_detail(self):
        """Test individual track detail"""
        try:
            response = requests.get(f"{self.base_url}/tracks/monza", timeout=10)
            if response.status_code == 200:
                track = response.json()
                success = (
                    track.get("track_id") == "monza" and
                    track.get("name") == "Autodromo Nazionale Monza" and
                    "corners" in track and
                    "braking_points" in track
                )
                self.log_result("GET /tracks/monza", success, "Monza track details")
            else:
                self.log_result("GET /tracks/monza", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /tracks/monza", False, str(e))

    def test_cars_endpoint(self):
        """Test cars endpoint - should return 35 cars total"""
        try:
            response = requests.get(f"{self.base_url}/cars", timeout=10)
            if response.status_code == 200:
                cars = response.json()
                success = len(cars) == 35
                self.log_result("GET /cars", success, f"Expected 35 cars, got {len(cars)}")
                
                # Test car categories
                f1_cars = [c for c in cars if c.get("category") == "F1"]
                gt3_cars = [c for c in cars if c.get("category") == "GT3"]
                gt4_cars = [c for c in cars if c.get("category") == "GT4"]
                
                self.log_result("F1 Cars Count", len(f1_cars) == 10, f"Expected 10 F1 cars, got {len(f1_cars)}")
                self.log_result("GT3 Cars Count", len(gt3_cars) == 14, f"Expected 14 GT3 cars, got {len(gt3_cars)}")
                self.log_result("GT4 Cars Count", len(gt4_cars) == 11, f"Expected 11 GT4 cars, got {len(gt4_cars)}")
                
                # Test car structure
                if cars:
                    car = cars[0]
                    required_fields = ['car_id', 'name', 'category', 'manufacturer', 'power_hp', 'top_speed']
                    missing_fields = [field for field in required_fields if field not in car]
                    self.log_result("Car Data Structure", len(missing_fields) == 0,
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /cars", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /cars", False, str(e))

    def test_cars_category_filter(self):
        """Test cars endpoint with category filter"""
        try:
            response = requests.get(f"{self.base_url}/cars?category=gt3", timeout=10)
            if response.status_code == 200:
                cars = response.json()
                success = len(cars) == 14 and all(c.get("category") == "GT3" for c in cars)
                self.log_result("GET /cars?category=gt3", success, f"Expected 14 GT3 cars, got {len(cars)}")
            else:
                self.log_result("GET /cars?category=gt3", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /cars?category=gt3", False, str(e))

    def test_telemetry_endpoint(self):
        """Test telemetry endpoint"""
        try:
            response = requests.get(f"{self.base_url}/telemetry/monza/ferrari_296_gt3", timeout=10)
            if response.status_code == 200:
                data = response.json()
                success = (
                    data.get("track_id") == "monza" and
                    data.get("car_id") == "ferrari_296_gt3" and
                    "data_points" in data and
                    "summary" in data and
                    len(data.get("data_points", [])) > 0
                )
                self.log_result("GET /telemetry/monza/ferrari_296_gt3", success, "Telemetry data structure")
                
                # Test data point structure
                if data.get("data_points"):
                    point = data["data_points"][0]
                    required_fields = ['distance', 'speed', 'throttle', 'brake', 'gear']
                    missing_fields = [field for field in required_fields if field not in point]
                    self.log_result("Telemetry Data Point Structure", len(missing_fields) == 0,
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /telemetry/monza/ferrari_296_gt3", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /telemetry/monza/ferrari_296_gt3", False, str(e))

    def test_quizzes_endpoint(self):
        """Test quizzes endpoint - should return 4 quizzes"""
        try:
            response = requests.get(f"{self.base_url}/quizzes", timeout=10)
            if response.status_code == 200:
                quizzes = response.json()
                success = len(quizzes) == 4
                self.log_result("GET /quizzes", success, f"Expected 4 quizzes, got {len(quizzes)}")
                
                # Test quiz structure
                if quizzes:
                    quiz = quizzes[0]
                    required_fields = ['quiz_id', 'title', 'category', 'difficulty', 'questions']
                    missing_fields = [field for field in required_fields if field not in quiz]
                    self.log_result("Quiz Data Structure", len(missing_fields) == 0,
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /quizzes", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /quizzes", False, str(e))

    def test_quiz_submit(self):
        """Test quiz submission"""
        try:
            # Submit answers for braking_basics quiz
            answers = {"1": 1, "2": 1, "3": 1, "4": 1}  # All correct answers
            response = requests.post(
                f"{self.base_url}/quizzes/braking_basics/submit",
                json={"answers": answers},
                timeout=10
            )
            if response.status_code == 200:
                result = response.json()
                success = (
                    "score" in result and
                    "total" in result and
                    "percentage" in result and
                    "results" in result
                )
                self.log_result("POST /quizzes/braking_basics/submit", success, 
                    f"Score: {result.get('score')}/{result.get('total')}")
            else:
                self.log_result("POST /quizzes/braking_basics/submit", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("POST /quizzes/braking_basics/submit", False, str(e))

    def test_news_endpoint(self):
        """Test news endpoint"""
        try:
            response = requests.get(f"{self.base_url}/news", timeout=10)
            if response.status_code == 200:
                news = response.json()
                success = len(news) > 0
                self.log_result("GET /news", success, f"Got {len(news)} news items")
                
                # Test news structure
                if news:
                    item = news[0]
                    required_fields = ['title', 'description', 'source', 'published']
                    missing_fields = [field for field in required_fields if field not in item]
                    self.log_result("News Data Structure", len(missing_fields) == 0,
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /news", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /news", False, str(e))

    def test_glossary_endpoint(self):
        """Test glossary endpoint"""
        try:
            response = requests.get(f"{self.base_url}/glossary", timeout=10)
            if response.status_code == 200:
                glossary = response.json()
                success = len(glossary) > 0
                self.log_result("GET /glossary", success, f"Got {len(glossary)} glossary terms")
                
                # Test glossary structure
                if glossary:
                    term = glossary[0]
                    required_fields = ['term', 'definition']
                    missing_fields = [field for field in required_fields if field not in term]
                    self.log_result("Glossary Data Structure", len(missing_fields) == 0,
                        f"Missing fields: {missing_fields}" if missing_fields else "")
            else:
                self.log_result("GET /glossary", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /glossary", False, str(e))

    def run_all_tests(self):
        """Run all backend API tests"""
        print("🏁 Starting Apex Academy Backend API Tests")
        print("=" * 50)
        
        # Test all endpoints
        self.test_api_root()
        self.test_tracks_endpoint()
        self.test_track_detail()
        self.test_cars_endpoint()
        self.test_cars_category_filter()
        self.test_telemetry_endpoint()
        self.test_quizzes_endpoint()
        self.test_quiz_submit()
        self.test_news_endpoint()
        self.test_glossary_endpoint()
        
        # Print summary
        print("\n" + "=" * 50)
        print(f"📊 Test Results: {self.tests_passed}/{self.tests_run} passed")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for failure in self.failed_tests:
                print(f"  - {failure}")
        
        success_rate = (self.tests_passed / self.tests_run * 100) if self.tests_run > 0 else 0
        print(f"📈 Success Rate: {success_rate:.1f}%")
        
        return self.tests_passed == self.tests_run

def main():
    tester = ApexAcademyAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())