from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="projectdb"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Hello"


@app.route('/skiType',methods=['GET'])
def get_customer_info():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

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
@app.route('/customer',methods=['GET', 'POST', 'PUT'])
def customer_info():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        customer_info= cur.execute("SELECT * FROM `customer`")

        if customer_info >0:
            customer_info = cur.fetchall()

        cur.close()
        return jsonify(customer_info),201

    elif request.method == 'PUT':
        data = request.get_json()
        customer_id=data['customerID']
        start_of_contract=data['startDate']

        cur=mysql.connection.cursor()

        change_startDate = cur.execute("UPDATE `customer` SET `startDate`=%s WHERE `customerID`=%s",(start_of_contract,customer_id,))
        mysql.connection.commit()

        customer_info= cur.execute("SELECT * FROM `customer`")

        if customer_info >0:
            customer_info = cur.fetchall()

        cur.close()
        return jsonify(customer_info),201

    elif request.method == 'POST':
        data = request.get_json()
        customer_id=data['customerID']
        name=data['name']
        dob=data['dateOfBirth']
        club=data['club']
        annual_skies=data['annual_skies']

        cur=mysql.connection.cursor()

        team_skier_info = cur.execute("SELECT * FROM `teamskier` WHERE `customerID`=%s", (customer_id,))

        if team_skier_info <= 0:
            change_teamskier_info = cur.execute("INSERT INTO `teamskier` (`customerID`, `name`, `dateOfBirth`, `club`, `annual_skies`) VALUES (%s,%s,%s,%s,%s)", (customer_id, name, dob, club, annual_skies))
            mysql.connection.commit()

            team_skier_info1 = cur.execute("SELECT * FROM `teamskier`")

            if team_skier_info1 > 0:
                team_skier_info1 = cur.fetchall()

            cur.close()
            return jsonify(team_skier_info1),201
        else : 
            cur.close()
            return "Team Skier with that customerID already exists"

    else:
        print("Method not implemented! Choose between GET, POST or PUT instead")
    
    
#                       #
#   Employee endpoints  #
#                       #
@app.route('/customer_rep', methods = ['GET','POST','PUT'])
def customer_rep():

    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        order_info= cur.execute("SELECT * FROM `orders`")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    elif request.method == 'PUT':
        data = request.get_json()
        order_number=data['order_number']
        state_of_order=data['state']

        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`=%s WHERE `orderNumber`=%s",(state_of_order,order_number))
        mysql.connection.commit()

        order_info= cur.execute("SELECT * FROM `orders`")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    elif request.method == 'POST':
        data = request.get_json()
        shipment_number=data['shipment_number']
        order_number=data['order_number']
        transporter_id=data['transporterID']
        customer_id=data['customerID']
        shipping_address=data['address']
        pick_up_date=data['date']
        state=data['state']

        cur=mysql.connection.cursor()

        shipment_info= cur.execute("SELECT * FROM `shipment` WHERE `shipmentNumber`=%s", (shipment_number))

        if shipment_info <=0:
            change_state = cur.execute("INSERT INTO `shipment` (`shipmentNumber`, `orderNumber`, `transporterID`, `customerID`, `shippingAddress`, `pickUpDate`, `state`) VALUES (%s, %s, %s, %s, %s, %s, %s)", (shipment_number, order_number, transporter_id, customer_id, shipping_address, pick_up_date, state,))
            mysql.connection.commit()

            shipments_info= cur.execute("SELECT * FROM `shipment`")

            if shipments_info >0:
                shipments_info = cur.fetchall()

            cur.close()
            return jsonify(shipments_info),201
        else :
            cur.close()
            return "A shipment with this shipment number already exists"
            
    else:
        print("Method not implemented! Choose between GET, PUT or POST instead")

   
@app.route('/storekeeper', methods = ['GET','POST','PUT'])
def storekeeper():

    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        order_info= cur.execute("SELECT * FROM `orders` WHERE `state` = 'available'")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    elif request.method == 'POST':
        data = request.get_json()
        order_number=data['order_number']
        state_of_order=data['state']

        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`=%s WHERE `orderNumber`=%s",(state_of_order,order_number))
        mysql.connection.commit()

        order_info= cur.execute("SELECT * FROM `orders`")

        if order_info >0:
            order_info = cur.fetchall()

        cur.close()
        return jsonify(order_info),201

    else:
        print("Method not implemented! Choose between GET or POST instead")


@app.route('/production_planner', methods = ['GET','PUT'])
def production_planner():

    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        plan_info= cur.execute("SELECT * FROM `productionplan`")

        if plan_info >0:
            plan_info = cur.fetchall()

        cur.close()
        return jsonify(plan_info),201

    else:
        print("Method not implemented! Choose between GET or POST instead")
    

""" 
@app.route('/change_skiType_info',methods=['POST'])
def change_customer_info():
    
    if request.method == 'POST':
        data = request.get_json()
        typeID=data['typeID']
        type=data['type']
        #model=data['model']
        #description=data['description']
        historical=data['historical']
        #url=data['url']
        #msrp=data['msrp']

        cur=mysql.connection.cursor()

        change_order_state = cur.execute("UPDATE `customer` SET `historical`=%s WHERE `type`=%s AND `typeID`=%s",(historical,type,typeID,))
        mysql.connection.commit()

        account_info= cur.execute("SELECT * FROM `skiType`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201

 """
""" 
@app.route('/get_customer_info',methods=['GET'])
def get_customer_info():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        account_info= cur.execute("SELECT * FROM `customer`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201


@app.route('/change_customer_info',methods=['POST'])
def change_customer_info():
    
    if request.method == 'POST':
        data = request.get_json()
        customer_id=data['customer_id']
        customer_name=data['customer_name']
        #startDate=data['startDate']
        #endDate=data['endDate']
        address=data['address']

        cur=mysql.connection.cursor()

        change_order_state = cur.execute("UPDATE `customer` SET `address`=%s WHERE `customer_name`=%s AND `customer_id`=%s",(address,customer_name,customer_id,))
        mysql.connection.commit()

        account_info= cur.execute("SELECT * FROM `customer`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201
 """


if __name__ == '__main__':
    app.run(debug=True)