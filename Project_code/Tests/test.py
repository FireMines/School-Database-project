import unittest
import requests

class Test_API(unittest.TestCase):
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    CUSTOMER_GET_API_URL = "http://127.0.0.1:5000/customer"   
    GET_PRODUCT_MODEL_API_URL = "http://127.0.0.1:5000/customer_rep"           
    DELETE_GIVEN_ORDER_POST_API_URL = "http://127.0.0.1:5000/storekeeper"     
    UPDATE_STATE_OF_SHIPMENT_POST_API_URL = "http://127.0.0.1:5000/production_planner"  

    CUSTOMER_LOGIN_INFO = {
        "username": "User1",
        "password": "password1"
    }
    
    GET_CUSTOMER_API_TEST = {
        "customer_id":1
    }
    
    GET_CUSTOMER_FILTER_API_TEST = {
        "customer_id": 1,
        "orderNumber": 20
    }
    
    GET_CUSTOMER_FOURWEEK_API_TEST = {    
        "startDate": "2022-05-26 16:03:00"
    }
    
    POST_CUSTOMER_API_TEST = {                                                 
        "customer_id": 1,
        "orderNumber": 2050,
        "quantity": 10,
        "productID": 2                                          
    }
    
    PUT_CUSTOMER_API_TEST = {
        "customer_id": 1,
        "orderNumber": 12100
    }
    
    DELETE_CUSTOMER_API_TEST = {
    "customer_id": 1,
    "orderNumber": 15
    }    

    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_INPUT = { 
                                                           
    "shipment_number":"222",
                                            
    }
    
    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_INCORRECT_INPUT = {
        
    "shipment_number":"222"
    }
    
    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_OUTPUT = "Shipment 222 has been updated"
    
        
    def test_1_check_get_api(self):
        response = requests.get(Test_API.LOGIN_API_URL, json=Test_API.CUSTOMER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)


        response = requests.get(Test_API.CUSTOMER_GET_API_URL, json=Test_API.GET_CUSTOMER_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)
        
    def test_2_check_get_api(self):
        response = requests.get(Test_API.LOGIN_API_URL, json=Test_API.CUSTOMER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)

        
        response = requests.get(Test_API.GET_PRODUCT_MODEL_API_URL, json=Test_API.GET_CUSTOMER_FILTER_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)
        
    def test_3_check_get_api(self):
        response = requests.get(Test_API.LOGIN_API_URL, json=Test_API.CUSTOMER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)

        
        response = requests.post(Test_API.DELETE_GIVEN_ORDER_POST_API_URL, json=Test_API.GET_CUSTOMER_FOURWEEK_API_TEST)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), Test_API.DELETE_CUSTOMER_API_TEST )
    
#    def test_4_check_post_incorrect_input_api(self):
#        
#       response = requests.post(Test_API.DELETE_GIVEN_ORDER_POST_API_URL, json=Test_API.PUT_CUSTOMER_API_TEST)
#       self.assertEqual(response.headers["Content-Type"],"application/json")
#       self.assertEqual(response.status_code, 404)
#    def test_5_check_post_correct_input_api(self):
#        
#        response = requests.post(Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_URL, json=Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_INPUT)
#        self.assertEqual(response.headers["Content-Type"],"application/json")
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response.json(), Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_OUTPUT )
#    
#    def test_6_check_post_incorrect_input_api(self):
#        
#       response = requests.post(Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_URL, json=Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_INCORRECT_INPUT)
#       self.assertEqual(response.headers["Content-Type"],"application/json")
#       self.assertEqual(response.status_code, 404)
#        
