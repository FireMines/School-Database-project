import unittest
import requests

class Test_API(unittest.TestCase):
    SKIS_AVAILABLE_GET_API_URL = "http://127.0.0.1:5000/get_skis_available"   
    GET_PRODUCT_MODEL_API_URL = "http://127.0.0.1:5000/get_products_model"           
    DELETE_GIVEN_ORDER_POST_API_URL = "http://127.0.0.1:5000/delete_given_order"     
    UPDATE_STATE_OF_SHIPMENT_POST_API_URL = "http://127.0.0.1:5000/UpdateStateOfShipment"  
    
    GET_PROUCT_MODEL_API_TEST_JSON_CORRECT_INPUT = {
        
        "model":"Redline"
        
    }
    
    GET_PRODUCT_MODEL_API_TEST_JSON_INCORRECT_INPUT = {
        
        "model":"Speedy"
        
    }
    
    GET_PRODUCT_MODEL_API_TEST_JSON_CORRECT_OUTPUT = {"22222", "Redline", "classic", "144", "beginner", "0", "url", "4000.0"}
    
    DELETE_GIVEN_ORDER_POST_API_TEST_JSON_CORRECT_INPUT = { 
                                                           
    "order_no":"9101",
                                            
    }
    
    DELETE_GIVEN_ORDER_POST_API_TEST_JSON_INCORRECT_INPUT = {
        
    "order_no":"0"
    }
    
    DELETE_GIVEN_ORDER_POST_API_TEST_JSON_CORRECT_OUTPUT = "Order 9101 was deleted from database"
    
    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_INPUT = { 
                                                           
    "shipment_number":"222",
                                            
    }
    
    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_INCORRECT_INPUT = {
        
    "shipment_number":"222"
    }
    
    UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_OUTPUT = "Shipment 222 has been updated"
    
        
    def test_1_check_get_api(self):
        
        response = requests.get(Test_API.SKIS_AVAILABLE_GET_API_URL)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)
        
    def test_2_check_get_api(self):
        
        response = requests.get(Test_API.GET_PRODUCT_MODEL_API_URL)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code,200)
        
    def test_3_check_post_correct_input_api(self):
        
        response = requests.post(Test_API.DELETE_GIVEN_ORDER_POST_API_URL, json=Test_API.DELETE_GIVEN_ORDER_POST_API_TEST_JSON_CORRECT_INPUT)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), Test_API.DELETE_GIVEN_ORDER_POST_API_TEST_JSON_CORRECT_OUTPUT )
    
    def test_4_check_post_incorrect_input_api(self):
        
       response = requests.post(Test_API.DELETE_GIVEN_ORDER_POST_API_URL, json=Test_API.DELETE_GIVEN_ORDER_POST_API_TEST_JSON_INCORRECT_INPUT)
       self.assertEqual(response.headers["Content-Type"],"application/json")
       self.assertEqual(response.status_code, 404)
    def test_5_check_post_correct_input_api(self):
        
        response = requests.post(Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_URL, json=Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_INPUT)
        self.assertEqual(response.headers["Content-Type"],"application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_CORRECT_OUTPUT )
    
    def test_6_check_post_incorrect_input_api(self):
        
       response = requests.post(Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_URL, json=Test_API.UPDATE_STATE_OF_SHIPMENT_POST_API_TEST_JSON_INCORRECT_INPUT)
       self.assertEqual(response.headers["Content-Type"],"application/json")
       self.assertEqual(response.status_code, 404)
        
