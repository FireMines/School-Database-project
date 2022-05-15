from asyncio.windows_events import NULL
import http
from types import NoneType
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import Customer.customer_endpoint as customer_endpoint
import Customer_rep.customerrep_endpoint as customerrep_endpoint
import ProductionPlanner.productionplanner_endpoint as productionplanner_endpoint
import Utility.public_endpoint as public_endpoint
import Utility.register_endpoint as register_endpoint
import Utility.login_endpoint as login_endpoint
import Transporter.transporter_endpoint as transporter_endpoint
import Storekeeper.storkeeper_endpoint as storkeeper_endpoint
import consts

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="projectdb"

sql = MySQL(app)

#                       #
#   Public Endpoint     #
#                       #
@app.route('/')
def public(): return public_endpoint.get_skitype_info()
    
#                                   #
#   transporter/shipping endpoint   #
#                                   #
@app.route('/transporter',methods=['GET', 'PUT'])
def transporter():
    if consts.userRole == "Transporter": 
        return transporter_endpoint.get_transporter_info()
    else: 
        return "Do not have permissions for this endpoint", http.HTTPStatus.UNAUTHORIZED

#                       #
#   Customer endpoint   #
#                       #
@app.route('/customer',methods=['GET', 'POST', 'PUT', 'DELETE'])
def customer(): 
    if consts.userRole == "Customer":
        return customer_endpoint.customer_info()  
    else:
        return "Do not have permissions for this endpoint", http.HTTPStatus.UNAUTHORIZED
        
#                               #
#   Customer rep endpoints      #
#                               #
@app.route('/customer_rep', methods = ['GET','POST','PUT'])
def customer_representative():
    if consts.userRole == "Customer_rep":
        return customerrep_endpoint.customer_rep()
    else:
        return "Do not have permissions for this endpoint", http.HTTPStatus.UNAUTHORIZED

#                               #
#   Storekeeper endpoints       #
#                               #  
@app.route('/storekeeper', methods = ['GET','POST','PUT'])
def storekeeper(): 
    if consts.userRole == "Storekeeper":
        return storkeeper_endpoint.storekeeper()
    else:
        return "Do not have permissions for this endpoint", http.HTTPStatus.UNAUTHORIZED

#                                   #
#   Production planner endpoints    #
#                                   #
@app.route('/production_planner', methods = ['GET','POST'])
def production_planner():
    if consts.userRole == "Production_planner":
        return productionplanner_endpoint.production_planner()
    else:
        return "Do not have permissions for this endpoint", http.HTTPStatus.UNAUTHORIZED

#                      #
#   login endpoints    #
#                      #
@app.route('/login', methods=['POST'])
def login(): return login_endpoint.loggingIn()

#                         #
#   register endpoints    #
#                         #
@app.route('/register', methods=['POST'])
def register(): return register_endpoint.registering()

if __name__ == '__main__':
    app.run(debug=True)