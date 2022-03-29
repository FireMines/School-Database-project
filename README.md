# Database_Project

This is the work of group 17

## How to run the Database_Project
To run the database project, you got to have some things installed on your computer. 
What you need is:
* Xampp Control Panel
* Anaconda Python
* Postman
* IDE Environment, we are using Visual Studio Code
* Cloned repo to your computer

After you have made sure you have all those things downloaded and setup you can start to run the program.
First you need to open up Xampp and press `Start` on _Apache_ and _MySQL_, then when this is done press `Admin` on _MySQL_. Now onto the next point.
Start by opening a terminal in the project folder, then type : `& C:\Database_Project\virt_env\Scripts\Activate.ps1` and press enter. After you have done this, you should see something among the lines of `(virt_env) PS C:\Database_Project>`. When this is done, simply write `python Project_code/main.py` in your terminal and press enter.
When all this is done, open up _Postman_ and enter the GET, POST, PUT or DELETE endpoints of your choosing. **NB!** Remember to start the address in Postman with the default url followed by the endpoint you want.

If no 

## Endpoint overview

### Default url: http://127.0.0.1:5000/


#### Public Endpoint (/skiType):
    methods: GET
    data: model, type, size, description, historical, url FROM ski_type


#### Customer Endpoint (/customer):
    method: GET, POST, PUT, DELETE
    data: * FROM ski_order, start, end FROM production_plan

##### Example Endpoint commands in Postman:
Method: Get

URL: http://127.0.0.1:5000/customer


Method: Post

URL: http://127.0.0.1:5000/customer

Body:

    {
    "customerID": 1,
    "name": "Habbo Hotel",
    "dateOfBirth": "2014-03-05 12:23:34",
    "club": "FC Habbo Elite",
    "annual_skies": 5
    }

Method: PUT

URL: http://127.0.0.1:5000/customer

Body:

For teamskier:

    {
    "customerID": 17,
    "startDate": "2022-09-17 12:23:34",
    "name": "Per Person",
    "dateOfBirth": "2015-09-19 12:23:34",
    "club": "Test Club",
    "annual_skies": 50,
    }
For store:

    {  
    "customerID": 2,
    "name": "Hei Hei",
    "buying_price": 420,
    "shipping_address": "Habbos havn"
    }
For franchise:

    {
    "customerID": 10,
    "startDate": "2022-09-19 12:23:34",
    "name": "Hei Hei",
    "buying_price": 420,
    "shipping_address": "Habbos havn"
    }

Method: DELETE

URL: http://127.0.0.1:5000/customer

Body:

#### Transporter Endpoint (/transporter):
    method: GET, PUT
    data: * FROM shipment


#### Employee Endpoint:
###### Customer rep (/customer_rep): 
    methods: GET, PUT, POST
    data: * FROM ski_order, * FROM shipment

###### Storekeeper (/storekeeper):
    methods: GET, POST, PUT
    data: * FROM ski_order, * FROM product

###### Production Planner:
    methods: POST
    data: * FROM production_plan
