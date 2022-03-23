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

        account_info= cur.execute("SELECT * FROM `skiType`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201

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