import unittest
import requests
import http

class Test_API(unittest.TestCase):

    # URLS used in tests
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    storekeeper_GET_API_URL = "http://127.0.0.1:5000/storekeeper"   

    # Input data sendt with

    storekeeper_LOGIN_INFO = {
        "username": "User4",
        "password": "password4"
    }
        
    POST_storekeeper_API_TEST = {                                                 
        "typeID":"400", 
        "type":"classic",
        "model":"active",
        "decription":"These are skies",
        "image":"None",
        "msrp":"200,50",
        "productID":"100000",
        "length":"147",
        "weight":"20-30"    
    }
    
    PUT_storekeeper_API_TEST = {
        "order_number":10000
    }
    
    # The test itself which runs everything       
    def testAll(self):
        testdata = {
            "get_storekeeper" : {
                "url" : Test_API.storekeeper_GET_API_URL,
                "json" : None,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get  
            },
            "post_storekeeper" : {
                "url" : Test_API.storekeeper_GET_API_URL,
                "json" : Test_API.POST_storekeeper_API_TEST,
                "expectedCode" : http.HTTPStatus.BAD_REQUEST, #Created if data is new, if test has been run, change to Bad Request
                "expectedValue" : None, 
                "method" : requests.post     
            },
            "put_storekeeper" : {
                "url" : Test_API.storekeeper_GET_API_URL,
                "json" : Test_API.PUT_storekeeper_API_TEST,
                "expectedCode" : http.HTTPStatus.BAD_REQUEST, #Created if data is new, if test has been run, change to Bad Request
                "expectedValue" : None, 
                "method" : requests.put     
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
        response = requests.post(Test_API.LOGIN_API_URL, json=Test_API.storekeeper_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)        
        

# Runs the tests here
test = Test_API()
test.testAll()

