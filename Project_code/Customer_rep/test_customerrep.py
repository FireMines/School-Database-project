import unittest
import requests
import http

class Test_API(unittest.TestCase):
    LOGIN_API_URL = "http://127.0.0.1:5000/login"
    customerrep_GET_API_URL = "http://127.0.0.1:5000/customer_rep"   

    customerrep_LOGIN_INFO = {
        "username": "User3",
        "password": "password3"
    }
        
    GET_customerrep_filtered_API_TEST = {
        "state": "available"
    }
    
    POST_customerrep_API_TEST = {                                                 
        "shipment_number":"2",
        "order_number": "200200",
        "transporterID":"1",
        "address":"FC Habbo",
        "date": "2022-05-26 16:03:00"   
    }
    
    PUT_customerrep_API_TEST = {
        "order_number":10000
    }
    
       
    def testAll(self):
        testdata = {
            "get_customerrep" : {
                "url" : Test_API.customerrep_GET_API_URL,
                "json" : None,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get  
            },
            "get_customerrep_filtered" : {
                "url" : Test_API.customerrep_GET_API_URL,
                "json" : Test_API.GET_customerrep_filtered_API_TEST,
                "expectedCode" : http.HTTPStatus.OK,
                "expectedValue" : None, 
                "method" : requests.get  
            },
            "post_customerrep" : {
                "url" : Test_API.customerrep_GET_API_URL,
                "json" : Test_API.POST_customerrep_API_TEST,
                "expectedCode" : http.HTTPStatus.BAD_REQUEST, #Created if data is new, if test has been run, change to Bad Request
                "expectedValue" : None, 
                "method" : requests.post     
            },
            "put_customerrep" : {
                "url" : Test_API.customerrep_GET_API_URL,
                "json" : Test_API.PUT_customerrep_API_TEST,
                "expectedCode" : http.HTTPStatus.BAD_REQUEST, #Created if data is new, if test has been run, change to Bad Request
                "expectedValue" : None, 
                "method" : requests.put     
            }
        }

        for _, data in testdata.items():
            Test_API.login(self)

            response = data["method"](data["url"], json=data["json"])
            self.assertEqual(response.headers["Content-Type"],"application/json")
            self.assertEqual(response.status_code,data["expectedCode"])
            expectedValue = data["expectedValue"]
            if expectedValue != None:
                self.assertEqual(response.json(), expectedValue)



    def login(self):
        response = requests.post(Test_API.LOGIN_API_URL, json=Test_API.customerrep_LOGIN_INFO)
        self.assertEqual(response.headers["Content-Type"],"text/html; charset=utf-8")
        self.assertEqual(response.status_code,http.HTTPStatus.OK)        
        


test = Test_API()
test.testAll()

