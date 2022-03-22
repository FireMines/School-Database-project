# Database_Project

This is the work of group 17

## Endpoint overview

#### Public Endpoint:
    methods: GET
    data: model, type, size, description, historical, url FROM ski_type


#### Customer Endpoint:
    method: GET, POST, DELETE
    data: * FROM ski_order, start, end FROM production_plan


#### Transporter Endpoint:
    method: GET, PUT
    data: * FROM shipment


#### Employee Endpoint:
###### Customer rep: 
    methods: GET, PUT, POST
    data: * FROM ski_order, * FROM shipment

###### Storekeeper:
    methods: GET, POST, PUT
    data: * FROM ski_order, * FROM product

###### Production Planner:
    methods: POST
    data: * FROM production_plan
