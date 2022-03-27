# Database_Project

This is the work of group 17

## Endpoint overview

#### Public Endpoint (/skiType):
    methods: GET
    data: model, type, size, description, historical, url FROM ski_type


#### Customer Endpoint (/customer):
    method: GET, POST, DELETE
    data: * FROM ski_order, start, end FROM production_plan


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
