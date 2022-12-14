import unittest
import requests
import http

class Test_API(unittest.TestCase):

    # URLS used in tests
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    CUSTOMER_GET_API_URL = "http://127.0.0.1:5000/customer"   

    # Input data sendt with

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
        "orderNumber": 123,
        "quantity": 10,
        "productID": 2                                          
    }
    
    PUT_CUSTOMER_API_TEST = {
        "customer_id": 1,
        "orderNumber": 12100
    }
    
    DELETE_CUSTOMER_API_TEST = {
        "customer_id": 1,
        "orderNumber": 123
    }

    # Expected data returned after deleting a customer
    DELETE_CUSTOMER_API_TEST_REMAINING_DATA = [
            [
                20,
                1,
                10,
                "0.00",
                "new",
                "Thu, 05 May 2022 18:24:06 GMT",
                2
            ]
        ]
        
    # The test itself which runs everything    
    def testAll(self):
        testdata = {
            "get_customer" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.GET_CUSTOMER_API_TEST,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get  
            },
            "get_customer_filtered" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.GET_CUSTOMER_FILTER_API_TEST,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get  
            },
            "get_customer_fourweek" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.GET_CUSTOMER_FOURWEEK_API_TEST,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get     
            },
            "post_customer" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.POST_CUSTOMER_API_TEST,
                "expectedCode" : http.HTTPStatus.CREATED, 
                "expectedValue" : None, 
                "method" : requests.post     
            },
            "put_customer" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.DELETE_CUSTOMER_API_TEST,
                "expectedCode" : http.HTTPStatus.BAD_REQUEST,
                "expectedValue" : None, 
                "method" : requests.put     
            },
            "delete_customer" : {
                "url" : Test_API.CUSTOMER_GET_API_URL,
                "json" : Test_API.DELETE_CUSTOMER_API_TEST,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.delete  
            }
        }

        # For loop which goes through every piece of data above and tests it automatically
        for _, data in testdata.items():
            Test_API.login(self)

            response = data["method"](data["url"], json=data["json"])
            self.assertEqual(response.headers["Content-Type"],"application/json")
            self.assertEqual(response.status_code,data["expectedCode"])
            expectedValue = data["expectedValue"]
            if expectedValue != None:
                self.assertEqual(response.json(), expectedValue)


    # Function to log in with the user needed to have access
    def login(self):
        response = requests.post(Test_API.LOGIN_API_URL, json=Test_API.CUSTOMER_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)        
        

# Runs the tests here
test = Test_API()
test.testAll()

