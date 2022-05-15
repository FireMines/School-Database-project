from asyncio.windows_events import NULL
from flask import request, jsonify
import consts
import http

#                               #
#   Storekeeper endpoints       #
#                               #
def storekeeper():

    #           #
    #   GET     #
    #           #
    if request.method == 'GET':
        
        cur=consts.mysql.connection.cursor()

        order_info= cur.execute("SELECT * FROM `orders` WHERE `state` = 'available'")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),http.HTTPStatus.OK

    #           #
    #   PUT     #
    #           #
    elif request.method == 'PUT':
        data = request.get_json()
        order_number=data['order_number']

        cur=consts.mysql.connection.cursor()

        order_info=cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s AND `state`='available'",(order_number,))

        if order_info >0:
            change_state = cur.execute("UPDATE `orders` SET `state`='ready' WHERE `orderNumber`=%s",(order_number,))
            consts.mysql.connection.commit()

            order_info= cur.execute("SELECT * FROM `orders`")

            if order_info >0:
                order_info = cur.fetchall()

            cur.close()
            return jsonify(order_info),http.HTTPStatus.CREATED

        else:
            cur.close()
            return jsonify("There is no order with this order number that is available to be ready to be shipped!"),http.HTTPStatus.BAD_REQUEST
        

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

        cur=consts.mysql.connection.cursor()

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
                consts.mysql.connection.commit()

            change_state = cur.execute("INSERT INTO `ski`(`productID`, `typeID`, `length`, `weight`) VALUES (%s, %s, %s, %s)", (product_id, type_id, ski_length, ski_weight,))
            consts.mysql.connection.commit()

            product_info= cur.execute("SELECT * FROM `ski`")

            if product_info >0:
                product_info = cur.fetchall()

            cur.close()
            return jsonify(product_info),http.HTTPStatus.CREATED
        else :
            cur.close()
            return jsonify("This product already exist in the database"),http.HTTPStatus.BAD_REQUEST

    else:
        print("Method not implemented! Choose between GET, PUT or POST instead")