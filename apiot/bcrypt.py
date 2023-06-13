from flask_bcrypt import Bcrypt 
from flask import current_app, g

def get_bcrypt():
    if 'bcrypt' not in g:
        g.bcrypt = Bcrypt(current_app)

    return g.bcrypt

def get_secret():
    return "api-iot-development"

