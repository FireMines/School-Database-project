from asyncio.windows_events import NULL
import http
from flask import request, jsonify
import consts

def loggingIn():
    if request.method == "POST":
        data = request.get_json()
        userName = data['username']
        password = data['password']

        foundUser = False
        dbPassword = ""

        cur=consts.mysql.connection.cursor()
        response = cur.execute("SELECT * FROM `authenticator` WHERE `Username`='" + userName + "';")

        if response > 0:
            foundUser = True
            userData = cur.fetchone() # -> only gets one row from db
            cur.close()

            dbPassword = userData[1] # The hashedpassword stored in the db
            consts.userRole = userData[2] # The role for the user

        if dbPassword == hashPassword(password) and foundUser:
            return "Logged in as " + consts.userRole, http.HTTPStatus.ACCEPTED
        else: 
            return "password/username not recognized", http.HTTPStatus.UNAUTHORIZED
    else: 
        return "Method not implemented", http.HTTPStatus.NOT_IMPLEMENTED


def hashPassword(password):
    hashedpass = password
    return hashedpass