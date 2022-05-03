from asyncio.windows_events import NULL
from flask import request, jsonify

#                               #
#   Customer rep endpoints      #
#                               #
def customer_rep(mysql):

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