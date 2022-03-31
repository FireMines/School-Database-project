from asyncio.windows_events import NULL
from types import NoneType
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="projectdb"

mysql = MySQL(app)

#                       #
#   Public Endpoint     #
#                       #
@app.route('/')
def get_skitype_info():
    
    if request.method == 'GET':
        data=request.get_json()
        
        cur=mysql.connection.cursor()

        if data:
            model_filter=data['model']
            skiType_info= cur.execute("SELECT * FROM `skiType` WHERE `model`=%s", (model_filter,))
        else:
            skiType_info= cur.execute("SELECT * FROM `skiType`")

        if skiType_info >0:
            skiType_info = cur.fetchall()

        cur.close()
        return jsonify(skiType_info),201
    
#                                   #
#   transporter/shipping endpoint   #
#                                   #
@app.route('/transporter',methods=['GET', 'PUT'])
def get_transporter_info():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        transporter_info= cur.execute("SELECT * FROM `shipment`")

        if transporter_info >0:
            transporter_info = cur.fetchall()

        cur.close()
        return jsonify(transporter_info),201
    
    elif request.method == 'PUT':
        data = request.get_json()
        shipmentNumber=data['shipmentNumber']
        transport_id=data['transporterID']
        status=data['state']

        cur=mysql.connection.cursor()

        change_order_state = cur.execute("UPDATE `shipment` SET `state`=%s WHERE `shipmentNumber`=%s AND `transporterID`=%s",(status,shipmentNumber,transport_id,))
        mysql.connection.commit()

        account_info= cur.execute("SELECT * FROM `shipment`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201
    
    
    else:
        print("Method not implemented! Choose between GET or POST instead")


#                       #
#   Customer endpoint   #
#                       #
@app.route('/customer',methods=['GET', 'POST', 'PUT', 'DELETE'])
def customer_info():
    
    if request.method == 'GET':
        data=request.get_json()

        cur=mysql.connection.cursor()

        if data:
            customer=data['customer_id']
            specific_order = data.get('orderNumber', "")
            since_filter = data.get('date', "")

            if since_filter != "":
                if specific_order != "":# and state:
                    customer_info= cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `date`>=%s",(specific_order,since_filter,))
                else: 
                    customer_info= cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s AND `date`>=%s",(customer,since_filter))
            else:
                if specific_order != "":# and state:
                    customer_info= cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s",(specific_order,))
                else: 
                    customer_info= cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s",(customer,))


        else:
            return "Remember to add your customerID",400

        if customer_info >0:
            customer_info = cur.fetchall()

        cur.close()
        return jsonify(customer_info),201

    elif request.method == 'PUT':

        data = request.get_json()
        customer_id=data['customer_id']
        orderNumber=data['orderNumber']

        cur=mysql.connection.cursor()

        order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))
        orderNumber_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (orderNumber,))

        if order_info > 0:
            if orderNumber_info > 0:
                checkIfAlreadyCancelled = cur.execute("SELECT `state` FROM `orders` WHERE `orderNumber`=%s",(orderNumber,))
                checkIfAlreadyCancelled = cur.fetchall()
                print(checkIfAlreadyCancelled)
                if checkIfAlreadyCancelled == 'cancelled': # Error here
                    cancell_order_info = cur.execute("UPDATE `orders` SET `state`='cancelled' WHERE `customer_id`=%s AND `orderNumber`=%s", (customer_id,orderNumber,))
                    mysql.connection.commit()

                    cancell_order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))

                    if cancell_order_info > 0:
                        cancell_order_info = cur.fetchall()
            
                    return jsonify(cancell_order_info),201
                else:
                    return "That order is already set to cancelled!",400
            else:
                return "That ordernumber already exists!",400

        else:
            cur.close()
            if order_info > 0:
                return "Unable to add a order, customerID does not exists!", 400
            else:
                return "Tried to create order with non existing customerID",400


        data = request.get_json()
        customer_id=data['customerID']
        start_of_contract=data['startDate']

        cur=mysql.connection.cursor()

        checkIfTeamSkier = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))
        checkIfIndivStore = cur.execute("SELECT * FROM `store` WHERE `customerID`=%s", (customer_id,))
        checkIfFranchise = cur.execute("SELECT * FROM `franchise` WHERE `customerID`=%s", (customer_id,))
        checkIfValidID = cur.execute("SELECT * FROM `customer` WHERE `customerID`=%s", (customer_id,))


        print("Skier: 1 Means exists, 0 means does not: ", checkIfTeamSkier)
        print("Store: 1 Means exists, 0 means does not: ", checkIfIndivStore)
        print("Franchise: 1 Means exists, 0 means does not: ", checkIfFranchise)

        print(checkIfValidID)
        if checkIfValidID <= 0:
            return "No customer with that ID!"

        if checkIfTeamSkier and checkIfIndivStore and checkIfFranchise < 0: 
            return "Not in any of its mandatory tables"


        if checkIfTeamSkier > 0:
            name=data['name']
            dob=data['dateOfBirth']
            club=data['club']
            annual_skies=data['annual_skies']

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateTeamSkier = cur.execute("UPDATE `teamskier` SET `name`=%s, `dateOfBirth`=%s, `club`=%s, `annual_skies`=%s WHERE `customerID`=%s",(name,dob,club,annual_skies,customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `teamskier`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


        if checkIfIndivStore > 0:
            name=data['name']
            price=data['price']
            address=data['address']

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateIndivStore = cur.execute("UPDATE `store` SET `name`=%s, `price`=%s, `address`=%s WHERE `customerID`=%s",(name,price,address,customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201

        if checkIfFranchise > 0:
            name=data['name']
            price=data['buying_price']
            address=data['shipping_address']

            checkIfFranchise_store = cur.execute("SELECT * FROM `franchise_store` WHERE `name`=%s", (name,))

            change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
            updateFranchise = cur.execute("UPDATE `franchise` SET `name`=%s, `buying_price`=%s, `shipping_address`=%s WHERE `customerID`=%s",(name,price,address,customer_id,))
            
            if checkIfFranchise_store > 0:
                shipping=data['shipping']
                updateFranchise_Store = cur.execute("UPDATE `franchise_store` SET `shipping`=%s WHERE `customerID`=%s",(shipping,customer_id,))

            
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `franchise`, `franchise_store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


    elif request.method == 'POST':
        data = request.get_json()
        customer_id=data['customer_id']
        orderNumber=data['orderNumber']
        quantity=data['quantity']
        productID=data['productID']

        cur=mysql.connection.cursor()

        order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))
        orderNumber_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (orderNumber,))

        if order_info > 0:
            if not orderNumber_info:
                checkProductID = cur.execute("SELECT * FROM `ski` WHERE `productID`=%s", (productID,))
                if not checkProductID:
                    return "ProductID which you are trying to order doesnt exist!"

                add_order_info = cur.execute("INSERT INTO `orders` (`customer_id`, `orderNumber`, `quantity`, `state`, `productID`) VALUES (%s,%s,%s,'new',%s)", (customer_id,orderNumber,quantity,productID,))
                mysql.connection.commit()

                ski_info = cur.execute("SELECT * FROM `ski` WHERE `productID`=%s", (productID,))

                add_order_info = cur.execute("SELECT * FROM `orders`")

                if add_order_info > 0:
                    add_order_info = cur.fetchall()
        
                return jsonify(add_order_info),201
            else:
                return "That ordernumber already exists!",400

        else:
            cur.close()
            if order_info > 0:
                return "Unable to add a order, customerID does not exists!", 400
            else:
                return "Tried to create order with non existing customerID",400

    elif request.method == 'DELETE':
        data = request.get_json()
        customer_id=data['customerID']
        start_of_contract=data['startDate']

        cur=mysql.connection.cursor()

        checkIfTeamSkier = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))
        checkIfIndivStore = cur.execute("SELECT * FROM `store` WHERE `customerID`=%s", (customer_id,))
        checkIfFranchise = cur.execute("SELECT * FROM `franchise` WHERE `customerID`=%s", (customer_id,))
        checkIfValidID = cur.execute("SELECT * FROM `customer` WHERE `customerID`=%s", (customer_id,))

        print("Skier: 1 Means exists, 0 means does not: ", checkIfTeamSkier)
        print("Store: 1 Means exists, 0 means does not: ", checkIfIndivStore)
        print("Franchise: 1 Means exists, 0 means does not: ", checkIfFranchise)

        print(checkIfValidID)
        if checkIfValidID <= 0:
            return "No customer with that ID!"

        if checkIfTeamSkier and checkIfIndivStore and checkIfFranchise < 0: 
            return "Not in any of its mandatory tables"


        if checkIfTeamSkier > 0:
            #name=data['name']
            #dob=data['dateOfBirth']
            #club=data['club']
            #annual_skies=data['annual_skies']

            deleteTeamSkier = cur.execute("DELETE FROM `teamskier` WHERE `teamskier`.`customerID` = %s",(customer_id,))
            deleteCustomer = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `teamskier`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


        if checkIfIndivStore > 0:
            #name=data['name']
            #price=data['price']
            #address=data['address']

            deleteIndivStore = cur.execute("DELETE FROM `store` WHERE `store`.`customerID` = %s",(customer_id,))
            deleteCustomer = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201

        if checkIfFranchise > 0:
            name=data['name']
            #price=data['buying_price']
            #address=data['shipping_address']

            checkIfFranchise_store = cur.execute("SELECT * FROM `franchise_store` WHERE `name`=%s", (name,))

            deleteFranchise = cur.execute("DELETE FROM `franchise` WHERE `franchise`.`customerID` = %s",(customer_id,))
            change_startDate = cur.execute("DELETE FROM `customer` WHERE `customer`.`customerID` = %s",(customer_id,))
            
            if checkIfFranchise_store > 0:
                shipping=data['shipping']
                deleteFranchise_Store = cur.execute("DELETE FROM `franchise_store` WHERE `franchise_store`.`name` = %s",(name,))

            
            mysql.connection.commit()

            customer_info= cur.execute("SELECT * FROM (`customer`, `franchise`, `franchise_store`)")

            if customer_info > 0:
                customer_info = cur.fetchall()

            cur.close()
            return jsonify(customer_info),201


    else:
        print("Method not implemented! Choose between GET, POST, PUT or DELETE instead")
    
    
#                               #
#   Customer rep endpoints      #
#                               #
@app.route('/customer_rep', methods = ['GET','POST','PUT'])
def customer_rep():

    #           #
    #   GET     #
    #           #
    if request.method == 'GET':
        data=request.get_json()

        cur=mysql.connection.cursor()

        if data:
            state= data['state']
            order_info= cur.execute("SELECT * FROM `orders` WHERE `state`=%s", (state,))
        else:
            order_info= cur.execute("SELECT * FROM `orders`")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    #           #
    #   PUT     #
    #           #
    elif request.method == 'PUT':
        data = request.get_json()
        order_number=data['order_number']
    
        cur=mysql.connection.cursor()

        order_info=cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `state` IN ('new', 'open')", (order_number,))

        if order_info >0:
            state_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `state`='new'", (order_number,))
            if state_info >0:
                change_state = cur.execute("UPDATE `orders` SET `state`='open' WHERE `orderNumber`=%s",(order_number,))
                mysql.connection.commit()
            else: 
                change_state = cur.execute("UPDATE `orders` SET `state`='available' WHERE `orderNumber`=%s",(order_number,))
                mysql.connection.commit()

            order_info=cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (order_number,))

            if order_info >0:
                order_info = cur.fetchall()

            cur.close()
            return jsonify(order_info),201

        else:
            cur.close()
            return "No orders with that order number that are new or open", 400

    #           #
    #   POST    #
    #           #
    elif request.method == 'POST':
        data = request.get_json()
        shipment_number=data['shipment_number']
        order_number=data['order_number']
        transporter_id=data['transporterID']
        shipping_address=data['address']
        pick_up_date=data['date']

        cur=mysql.connection.cursor()

        shipment_info= cur.execute("SELECT * FROM `shipment` WHERE `shipmentNumber`=%s", (shipment_number))
        order_info=cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (order_number,))
        transporter_info =cur.execute("SELECT * FROM `transporter` WHERE `transporterID`=%s", (transporter_id,))

        if shipment_info <=0 and (order_info and transporter_info >0):
            change_state = cur.execute("INSERT INTO `shipment` (`shipmentNumber`, `orderNumber`, `transporterID`, `shippingAddress`, `pickUpDate`, `state`) VALUES (%s, %s, %s, %s, %s, 'ready')", (shipment_number, order_number, transporter_id, shipping_address, pick_up_date,))
            mysql.connection.commit()

            shipments_info= cur.execute("SELECT * FROM `shipment` WHERE `shipmentNumber`=%s", (shipment_number,))

            if shipments_info >0:
                shipments_info = cur.fetchall()

            cur.close()
            return jsonify(shipments_info),201
        else :
            cur.close()
            if shipment_info >0:
                return "A shipment with this shipment number already exists",400
            else:
                return "Tried to create shipment with non existing order or transporter",400
            
    else:
        print("Method not implemented! Choose between GET, PUT or POST instead")

#                               #
#   Storekeeper endpoints       #
#                               #  
@app.route('/storekeeper', methods = ['GET','POST','PUT'])
def storekeeper():

    #           #
    #   GET     #
    #           #
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        order_info= cur.execute("SELECT * FROM `orders` WHERE `state` = 'available'")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    #           #
    #   PUT     #
    #           #
    elif request.method == 'PUT':
        data = request.get_json()
        order_number=data['order_number']

        cur=mysql.connection.cursor()

        order_info=cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `state`='available'",(order_number,))

        if order_info >0:
            change_state = cur.execute("UPDATE `orders` SET `state`='ready' WHERE `orderNumber`=%s",(order_number,))
            mysql.connection.commit()

            order_info= cur.execute("SELECT * FROM `orders`")

            if order_info >0:
                order_info = cur.fetchall()

            cur.close()
            return jsonify(order_info),201

        else:
            cur.close()
            return "There is no order with this order number that is available to be ready to be shipped!",400
        

    #           #
    #   POST    #
    #           #
    elif request.method == 'POST':
        data = request.get_json()
        #skiType data
        type_id = data['typeID']
        #product data
        product_id=data['productID']
        ski_length=data['length']
        ski_weight=data['weight']

        cur=mysql.connection.cursor()

        product_info= cur.execute("SELECT * FROM `ski` WHERE `productID`=%s", (product_id,))

        if product_info <=0:
            
            ski_type_info = cur.execute("SELECT * FROM `skitype` WHERE `typeID`=%s", (type_id,))

            if ski_type_info <=0:
                ski_type= data['type']
                model_type= data['model']
                ski_decription =data['decription']
                image_url = data['image']
                msrp = data['msrp']
                change_state = cur.execute("INSERT INTO `skitype`(`typeID`, `type`, `model`, `description`, `url`, `msrp`) VALUES (%s,%s,%s,%s,%s,%s)", (type_id, ski_type, model_type, ski_decription, image_url, msrp))
                mysql.connection.commit()

            change_state = cur.execute("INSERT INTO `ski`(`productID`, `typeID`, `length`, `weight`) VALUES (%s, %s, %s, %s)", (product_id, type_id, ski_length, ski_weight,))
            mysql.connection.commit()

            shipments_info= cur.execute("SELECT * FROM `ski`")

            if shipments_info >0:
                shipments_info = cur.fetchall()

            cur.close()
            return jsonify(shipments_info),201
        else :
            cur.close()
            return "This product already exist in the database",400

    else:
        print("Method not implemented! Choose between GET, PUT or POST instead")

#                                   #
#   Production planner endpoints    #
#                                   #
@app.route('/production_planner', methods = ['GET','POST'])
def production_planner():

    #           #
    #   GET     #
    #           #
    if request.method == 'GET':
        data=request.get_json()
        
        cur=mysql.connection.cursor()

        if data:
            plan_id =data['planID']
            plan_info= cur.execute("SELECT * FROM `productionplanreference` INNER JOIN `productionplan` ON `productionplanreference`.`planID`=`productionplan`.`planID` WHERE `productionplan`.`planID`=%s", (plan_id,))
        else:
            plan_info= cur.execute("SELECT * FROM `productionplan`")

        if plan_info >0:
            plan_info = cur.fetchall()

        cur.close()
        return jsonify(plan_info),201

    #           #
    #   POST    #
    #           #
    elif request.method == 'POST':
        data = request.get_json()
        plan_id = data['planID']
        employee_id = data['employeeID']
        start_date=data['startDate']
        end_date=data['endDate']
        referneces=data['planReferences']

        cur=mysql.connection.cursor()

        plan_info= cur.execute("SELECT * FROM `productionplan` WHERE `planID`=%s", (plan_id,))

        if plan_info <=0:
            
            change_state = cur.execute("INSERT INTO `productionplan` (`employeeNumber`, `planID`, `startDate`, `endDate`) VALUES (%s,%s,%s,%s)", (employee_id, plan_id, start_date, end_date,))
            mysql.connection.commit()

            for ref in referneces:
                ref_id=ref['referenceID']
                product_id=ref['productID']
                quantity=ref['quantity']

                change_state== cur.execute("INSERT INTO `productionplanreference` (`planID`, `productID`, `ReferenceID`, `Quantity`) VALUES (%s,%s,%s,%s)", (plan_id, product_id, ref_id, quantity,))
                mysql.connection.commit()

            plan_info= cur.execute("SELECT * FROM `productionplanreference` INNER JOIN `productionplan` ON `productionplanreference`.`planID`=`productionplan`.`planID` WHERE `productionplan`.`planID`=%s", (plan_id,))

            if plan_info >0:
                plan_info = cur.fetchall()

            cur.close()
            return jsonify(plan_info),201
        else :
            cur.close()
            return "This plan already exist in the database",400

    else:
        print("Method not implemented! Choose between GET or POST instead")


if __name__ == '__main__':
    app.run(debug=True)