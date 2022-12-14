from asyncio.windows_events import NULL
from flask import request, jsonify
import consts
import datetime
import http

#                       #
#   Customer endpoint   #
#                       #
def customer_info():
    
    if request.method == 'GET':
        data=request.get_json()

        cur=consts.mysql.connection.cursor()

        # If any data exists in input
        if data:
            # By doing data.get the input becomes optional depending on what you want to get
            customer=data.get('customer_id', "")
            specific_order = data.get('orderNumber', "")
            since_filter = data.get('date', "")
            startDate = data.get('startDate', "")
            today = datetime.date.today()
            first = today.replace(day=1)
            lastMonth = first - datetime.timedelta(days=21)


            # Filter what request you want to do
            if customer != "":  
                if since_filter != "":
                    if specific_order != "":    # Get a specific orders with a since filter
                        customer_info= cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `date`>=%s",(specific_order,since_filter,))

                    else:                       # Get all orders from a specific customer
                        customer_info= cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s AND `date`>=%s",(customer,since_filter))
                else:
                    if specific_order != "":    # Get all info from a specific order
                        customer_info= cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s",(specific_order,))
                    else:                       # Get all data from a customer
                        customer_info= cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s",(customer,))
            else:
                if startDate != "":            # Checks if there are any productions from the last month aka 4 weeks
                    productionplan = cur.execute("SELECT `planID` FROM `productionplan` WHERE `startDate`>=%s",(lastMonth,))
                    if productionplan > 0:      # Returns production plan for the last month
                        customer_info= cur.execute("SELECT * FROM `productionplanreference` WHERE `planID`=%s",(productionplan,))
                    else:
                        return jsonify("No productionplans for this ID!"),http.HTTPStatus.BAD_REQUEST
                else:
                    return jsonify("No start date added to find last 4 weeks production plans!"),http.HTTPStatus.BAD_REQUEST
        else:
            return jsonify("Remember to add your customerID"),http.HTTPStatus.BAD_REQUEST

        if customer_info >0:
            customer_info = cur.fetchall()

        cur.close()
        return jsonify(customer_info),http.HTTPStatus.OK

    elif request.method == 'PUT':

        data = request.get_json()
        customer_id=data['customer_id']
        orderNumber=data['orderNumber']

        cur=consts.mysql.connection.cursor()

        order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))
        orderNumber_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (orderNumber,))

        # Check if any orders exists with inputed customer_id
        if order_info > 0:

            # Check if any orders exists with inputed ordernumber
            if orderNumber_info > 0: 
                checkIfAlreadyCancelled = cur.execute("SELECT `state` FROM `orders` WHERE `orderNumber`=%s",(orderNumber,))
                checkIfAlreadyCancelled = cur.fetchall()

                # Makes order cancelled if its not already
                if checkIfAlreadyCancelled == 'cancelled': 
                    cancell_order_info = cur.execute("UPDATE `orders` SET `state`='cancelled' WHERE `customer_id`=%s AND `orderNumber`=%s", (customer_id,orderNumber,))
                    consts.mysql.connection.commit()

                    cancell_order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))

                    if cancell_order_info > 0:
                        cancell_order_info = cur.fetchall()
            
                    return jsonify(cancell_order_info),http.HTTPStatus.CREATED
                else:
                    return jsonify("That order is already set to cancelled!"),http.HTTPStatus.BAD_REQUEST
            else:
                return jsonify("That ordernumber already exists!"),http.HTTPStatus.BAD_REQUEST

        else:
            cur.close()
            if order_info > 0:
                return jsonify("Unable to add a order, customerID does not exists!"), http.HTTPStatus.BAD_REQUEST
            else:
                return jsonify("Tried to create order with non existing customerID"),http.HTTPStatus.BAD_REQUEST

    elif request.method == 'POST':
        data = request.get_json()
        customer_id=data['customer_id']
        orderNumber=data['orderNumber']
        quantity=data['quantity']
        productID=data['productID']

        cur=consts.mysql.connection.cursor()

        order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))
        orderNumber_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (orderNumber,))

        # Check if any orders exists with inputed customer_id
        if order_info > 0:

            # Check if any orders exists with inputed ordernumber
            if not orderNumber_info:
                checkProductID = cur.execute("SELECT * FROM `ski` WHERE `productID`=%s", (productID,))

                # Check if any products exists with inputed productID
                if not checkProductID:
                    return jsonify("ProductID which you are trying to order doesnt exist!"), http.HTTPStatus.BAD_REQUEST

                add_order_info = cur.execute("INSERT INTO `orders` (`customer_id`, `orderNumber`, `quantity`, `state`, `productID`) VALUES (%s,%s,%s,'new',%s)", (customer_id,orderNumber,quantity,productID,))
                consts.mysql.connection.commit()

                ski_info = cur.execute("SELECT * FROM `ski` WHERE `productID`=%s", (productID,))

                add_order_info = cur.execute("SELECT * FROM `orders`")

                if add_order_info > 0:
                    add_order_info = cur.fetchall()
        
                return jsonify(add_order_info),http.HTTPStatus.CREATED
            else:
                return jsonify("That ordernumber already exists!"),http.HTTPStatus.BAD_REQUEST

        else:
            cur.close()
            if order_info > 0:
                return jsonify("Unable to add a order, customerID does not exists!"), http.HTTPStatus.BAD_REQUEST
            else:
                return jsonify("Tried to create order with non existing customerID"),http.HTTPStatus.BAD_REQUEST

    elif request.method == 'DELETE':

        data = request.get_json()
        customer_id=data['customer_id']
        orderNumber=data['orderNumber']

        cur=consts.mysql.connection.cursor()

        order_info = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))
        orderNumber_info = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", (orderNumber,))

        # Check if any orders exists with inputed customer_id
        if order_info:

            # Check if any orders exists with inputed ordernumber
            if orderNumber_info > 0:
                    deleteOrder = cur.execute("DELETE FROM `orders` WHERE `orders`.`orderNumber` = %s",(orderNumber,))
                    consts.mysql.connection.commit()

                    deleteOrder = cur.execute("SELECT * FROM `orders` WHERE `customer_id`=%s", (customer_id,))

                    if deleteOrder > 0:
                        deleteOrder = cur.fetchall()
            
                    return jsonify(deleteOrder),http.HTTPStatus.OK
            else:
                return jsonify("That ordernumber does not exists!"),http.HTTPStatus.BAD_REQUEST
        else:
            return jsonify("CustomerID does not exist!"),http.HTTPStatus.BAD_REQUEST

    else:
        return jsonify("Method not implemented! Choose between GET, POST, PUT or DELETE instead"), http.HTTPStatus.NOT_IMPLEMENTED
    