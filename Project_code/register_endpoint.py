from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
import http
import random
from flask import request, jsonify
import consts
import login_endpoint

def registering():
    if request.method == "POST":
        data = request.get_json()
        userName = data['username']
        password = data['password']
        role = data ['Role']

        cur=consts.mysql.connection.cursor()
        response = cur.execute("SELECT * FROM `authenticator` WHERE `Username`='" + userName + "';")
        if response <= 0:
            salt =  randomSaltMaker()
            hash = login_endpoint.hashPassword(password, salt).hex()
            change_state = cur.execute("INSERT INTO `authenticator` (`Username`, `Hashedpassword`, `salt`, `role`) VALUES (%s, %s, %s, %s)", (userName, hash, salt, role))
            consts.mysql.connection.commit()
            print(hash)
            return "User registered", http.HTTPStatus.CREATED
        else:
            return "Username already taken", http.HTTPStatus.CONFLICT


def randomSaltMaker():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    return "".join(chars) # -> returns a random salt of length 16