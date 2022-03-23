from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="banking"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Hello"

@app.route('/get_customer_info',methods=['GET'])
def get_customer_info():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        account_info= cur.execute("SELECT * FROM `account`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201


@app.route('/change_customer_info',methods=['POST'])
def change_customer_info():
    
    if request.method == 'POST':
        data = request.get_json()
        account_number=data['account_number']
        customer_id=data['customer_id']
        status=data['status']

        cur=mysql.connection.cursor()

        change_order_state = cur.execute("UPDATE `account` SET `Status`=%s WHERE `account_number`=%s AND `customer_id`=%s",(status,account_number,customer_id,))
        mysql.connection.commit()

        account_info= cur.execute("SELECT * FROM `account`")

        if account_info >0:
            account_info = cur.fetchall()

        cur.close()
        return jsonify(account_info),201



if __name__ == '__main__':
    app.run(debug=True)