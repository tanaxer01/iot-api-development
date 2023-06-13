from flask import Blueprint, request, jsonify
from flask_expects_json import expects_json
from apiot.models.location import *
from apiot.utils import check_key 

location = Blueprint('location', __name__, template_folder='templates')

@location.route("/location/<api_key>/getAll")
def all(api_key):
    if res := one(id):
        return res, 200
    return "", 404

@location.route("/location/<api_key>/get/<id>")
def one(api_key, id):
    if res := one(id):
        return res, 200
    return "", 404

@location.route("/location/<api_key>/modify/<id>", methods=["PUT"])
@expects_json(modify_scheme)
def modify(api_key, id):
    if check_key(api_key) == False:
       return "API Key not valid", 500

    location_dict = request.json
    res = update(id, **location_dict)  

    return res, 201

@location.route("/location/<api_key>/delete/<id>", methods=["DELETE"])
@expects_json(modify_scheme)
def delete():
    pass
