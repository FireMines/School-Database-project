import unittest
import requests
import http

class Test_API(unittest.TestCase):
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    TRANSPORTER_URL = "http://127.0.0.1:5000/transporter"       

    TRANSPORTER_LOGIN_INFO = {
        "username": "User2",
        "password": "password2"
    }
    
    POST_TRANSPORTER_API_TEST = {                                                 
        "shipmentNumber": 1,
        "transporterID": 1,
        "state": "shipped"                                        
    }
    
    def login_transport(self):
        response = requests.post(Test_API.LOGIN_API_URL, json=Test_API.TRANSPORTER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)
        
    def test_1_check_get_api(self):
        Test_API.login_transport(self)

        response = requests.get(Test_API.TRANSPORTER_URL)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)
        
    def test_2_check_put_api(self):
        Test_API.login_transport(self)
        
        response = requests.put(Test_API.TRANSPORTER_URL, json=Test_API.POST_TRANSPORTER_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,http.HTTPStatus.CREATED)
        

test = Test_API()
test.test_1_check_get_api()
test.test_2_check_put_api()