from asyncio.windows_events import NULL
from types import NoneType
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import productionplanner_endpoint
import public_endpoint
import transporter_endpoint
import storkeeper_endpoint
import customerrep_endpoint
import customer_endpoint

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
def public(): return public_endpoint.get_skitype_info(mysql)
    
#                                   #
#   transporter/shipping endpoint   #
#                                   #
@app.route('/transporter',methods=['GET', 'PUT'])
def transporter(): return transporter_endpoint.get_transporter_info(mysql)

#                       #
#   Customer endpoint   #
#                       #
@app.route('/customer',methods=['GET', 'POST', 'PUT', 'DELETE'])
def customer(): return customer_endpoint.customer_info(mysql)  

    
#                               #
#   Customer rep endpoints      #
#                               #
@app.route('/customer_rep', methods = ['GET','POST','PUT'])
def customer_representative(): return customerrep_endpoint.customer_rep(mysql)

#                               #
#   Storekeeper endpoints       #
#                               #  
@app.route('/storekeeper', methods = ['GET','POST','PUT'])
def storekeeper(): return storkeeper_endpoint.storekeeper(mysql)

#                                   #
#   Production planner endpoints    #
#                                   #
@app.route('/production_planner', methods = ['GET','POST'])
def production_planner():  return productionplanner_endpoint.production_planner(mysql)

if __name__ == '__main__':
    app.run(debug=True)