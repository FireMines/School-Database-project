from asyncio.windows_events import NULL
from flask import request, jsonify
import consts

#                                   #
#   transporter/shipping endpoint   #
#                                   #
def get_transporter_info():
    
    if request.method == 'GET':
        
        cur=consts.mysql.connection.cursor()

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

        cur=consts.mysql.connection.cursor()

        change_order_state = cur.execute("UPDATE `shipment` SET `state`=%s WHERE `shipmentNumber`=%s AND `transporterID`=%s",(status,shipmentNumber,transport_id,))
        consts.mysql.connection.commit()

        account_info= cur.execute("SELECT * FROM `shipment`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201
    
    
    else:
        print("Method not implemented! Choose between GET or POST instead")
