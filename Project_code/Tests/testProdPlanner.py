import unittest
import requests
import http

class Test_API(unittest.TestCase):
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    PLANNER_URL = "http://127.0.0.1:5000/production_planner"       

    PLANNER_LOGIN_INFO = {
        "username": "User5",
        "password": "password5"
    }
    
    GET_PLANNER_API_TEST = {
        "planID":"1"
    }
    
    POST_PLANNER_API_TEST = {                                                 
        "planID":"2",
        "employeeID":"1",
        "startDate":"2022-02-01",
        "endDate":"2022-02-28",
        "planReferences":[
            {
                "referenceID":"4",
                "productID":"2",
                "quantity":"10"
            },
            {
                "referenceID":"5",
                "productID":"1",
                "quantity":"5"
            }
        ]                                      
    }
    
    def login_planner(self):
        response = requests.post(Test_API.LOGIN_API_URL, json=Test_API.PLANNER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)
        
    def test_1_check_get_api(self):
        Test_API.login_planner(self)

        response = requests.get(Test_API.PLANNER_URL)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)
        
    def test_2_check_get_api_filter(self):
        Test_API.login_planner(self)

        response = requests.get(Test_API.PLANNER_URL,json=Test_API.GET_PLANNER_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)
        
    def test_3_check_post_api(self):
        Test_API.login_planner(self)
        
        response = requests.post(Test_API.PLANNER_URL, json=Test_API.POST_PLANNER_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.BAD_REQUEST) ##BAD REQUEST IS INTENTIONAL
        

test = Test_API()
test.test_1_check_get_api()
test.test_2_check_get_api_filter()
test.test_3_check_post_api()