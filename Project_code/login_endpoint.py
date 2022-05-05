from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
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
            salt = userData[2]
            consts.userRole = userData[3] # The role for the user

        if dbPassword == hashPassword(password, salt).hex() and foundUser:
            return "Logged in as " + consts.userRole, http.HTTPStatus.ACCEPTED
        else: 
            return "password/username not recognized", http.HTTPStatus.UNAUTHORIZED
    else: 
        return "Method not implemented", http.HTTPStatus.NOT_IMPLEMENTED


def hashPassword(password, salt):
    our_app_iters = 500_000
    passwordAsByte = str.encode(password)
    saltAsByte = str.encode(salt)
    return pbkdf2_hmac('sha256',  passwordAsByte, saltAsByte, our_app_iters)

