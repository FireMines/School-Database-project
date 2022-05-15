# Database_Project

This is the work of group 17

## How to run the Database_Project
To run the database project, you got to have some things installed on your computer. 
What you need is:
* Xampp Control Panel
* Anaconda Python (the newest version of python is included in Anaconda)
* Postman (We've included a JSON file for import)
* IDE Environment, we are using Visual Studio Code
* Cloned repo to your computer

After you have made sure you have all those things downloaded and setup you can start to run the program.
First you need to open up Xampp and press `Start` on _Apache_ and _MySQL_, then when this is done press `Admin` on _MySQL_. Now onto the next point.
Start by opening a terminal in the project folder, then type : `& C:\Database_Project\virt_env\Scripts\Activate.ps1` and press enter. After you have done this, you should see something among the lines of `(virt_env) PS C:\Database_Project>`. When this is done, simply write `python Project_code/main.py` in your terminal and press enter.
When all this is done, open up _Postman_ and enter the GET, POST, PUT or DELETE endpoints of your choosing. **NB!** Remember to start the address in Postman with the default url followed by the endpoint you want.

In this README you'll see examples provided of how to interract with the database via postman. We have not implemented arguments via the URL so everything is strictly through postman.

## Endpoint overview

### Default url: http://127.0.0.1:5000/


#### Public Endpoint (/skiType):
    methods: GET
    data: SELECT * FROM ski

##### Example Endpoint commands in Postman:
Method: **Get**

URL: http://127.0.0.1:5000/

Body(Option1 filter by model only):

    {
    "model":"activePro"
    }

Body(Option2 filter by size only):

    {
    "size": "147"
    }

Body(Option3 filter by both model and size):

    {
    "model":"activePro",
    "size": "147"  
    }


#### Register Endpoint (/register):
    methods: POST
    data: SELECT * FROM authenticator

##### Example Endpoint commands in Postman:
Method: **Post**

URL: http://127.0.0.1:5000/register

Body: 

    {
    "username": "User6",
    "password": "password6",
    "Role": "Customer"
    }

The username must be unique in order for the new user to be registered.

#### Login Endpoint (/login)
    methods: POST
    data: SELECT role FROM authenticator

##### Example Endpoint commands in Postman:
method: **POST**

URL: http://127.0.0.1:5000/login

Body: 

    {
    "username": "User1",
    "password": "password1"
    }

After logging in as a user you will get all the permissions that the user has due to their saved role. 

##### Existing Users in the data base

User1 (Customer):
    {
    "username": "User1",
    "password": "password1"
    }

User2 (Transporter):
    {
    "username": "User2",
    "password": "password2"
    }

User3 (Customer_rep):
    {
    "username": "User3",
    "password": "password3"
    }

User4 (Storekeeper):
    {
    "username": "User4",
    "password": "password4"
    }

User5 (Production_planner):
    {
    "username": "User5",
    "password": "password5"
    }

#### Customer Endpoint (/customer):
    method: GET, POST, PUT, DELETE
    data: SELECT * FROM `orders`

##### Example Endpoint commands in Postman:
Method: **Get**

URL: http://127.0.0.1:5000/customer

Body:

If you want to search for customer and a specific ordernumber:

    {
    "customer_id": 1,
    "orderNumber": 5
    }

If you want to search for customer and all its orders:

    {
    "customer_id": 1
    }

If you want to search for customer and a specific ordernumber with a since filter:

    {
    "customer_id": 1,
    "orderNumber": 5,
    "date": "2022-03-30 12:23:34"
    }

If you want to retrieve a four week production plan summary from a specific date:

    {
    "startDate": "2022-05-26 16:03:00"
    }

Method: **Post**

URL: http://127.0.0.1:5000/customer

Body:

    {
    "customer_id": 1,
    "orderNumber": 20,
    "quantity": 10,
    "productID": 2
    }

Method: **PUT**

URL: http://127.0.0.1:5000/customer

Body:

    {
    "customer_id": 1,
    "orderNumber": 12
    }

Method: **DELETE**

URL: http://127.0.0.1:5000/customer

Body:

    {
    "customer_id": 1,
    "orderNumber": 15
    }


#### Transporter Endpoint (/transporter):
    method: GET, PUT
    data: SELECT * FROM shipment
##### Example Endpoint commands in Postman:
Method: GET

URL: http://127.0.0.1:5000/transporter

Body(optional):

    {
    "shipmentNumber": "1"
    }

Method: PUT

URL: http://127.0.0.1:5000/transporter

Body:

    {
    "shipmentNumber": "2",
    "state": "ready"
    }

This also changes the order's state to the same as the shipment, but doesnt reveal it as the transporter doesn't need to view the order itself.

#### Employee Endpoint:
###### Customer rep (/customer_rep): 
    methods: GET, PUT, POST
    data: SELECT * FROM order, SELECT * FROM shipment

##### Example Endpoint commands in Postman:
Method: GET

URL: http://127.0.0.1:5000/customer_rep

Body(optional):

    {
    "state": "available"
    }

Method: PUT

URL: http://127.0.0.1:5000/customer_rep

Body:

    {
    "order_number": "100100"
    }

Method: POST

URL: http://127.0.0.1:5000/customer_rep

Body:

    {
    "shipment_number":"2",
    "order_number": "100100",
    "transporterID":"1",
    "address":"FC Habbo",
    "date": "2022-05-26 16:03:00"
    }

Note: order_number and transporterID needs to be existing within the database for this body to work

###### Storekeeper (/storekeeper):
    methods: GET, POST, PUT
    data: SELECT * FROM orders WHERE state=available, SELECT * FROM product, SELECT * FROM ski_type

Method: GET

URL: http://127.0.0.1:5000/storekeeper

Method: PUT

URL: http://127.0.0.1:5000/storekeeper

Body:

    {
    "order_number":"100100"
    }

Method: POST

URL: http://127.0.0.1:5000/storekeeper

Body(Option 1):

    {
    "typeID":"4", 
    "type":"classic",
    "model":"active",
    "decription":"These are skies",
    "image":"None",
    "msrp":"200,50",
    "productID":"10",
    "length":"147",
    "weight":"20-30"
    }

Body(Option 2):

    {
    "typeID":"4", 
    "productID":"10",
    "length":"147",
    "weight":"20-30"
    }

Note: for the body option 2 the database need to have a already existing ski_type with the typeID provided

###### Production Planner:
    methods: GET, POST
    data: SELECT * FROM production_plan, SELECT * FROM productionPlanReference

Method: GET

URL: http://127.0.0.1:5000/production_planner

Body(Optional):

    {
    "planID":"1"
    }

Note: If the get request is not followed with a specific planID it will show a summary of all plans in the database, however when searching for a specific plan it will git the productionPlan references to that plan as well.

Method: POST

URL: http://127.0.0.1:5000/production_planner

Body:

    {
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

Note: EmployeeID need to be an existing employee in the database


