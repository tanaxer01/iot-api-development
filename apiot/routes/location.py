from flask import Blueprint, request
from apiot.models.location import *
from apiot.utils import check_company_key

location = Blueprint('location', __name__, template_folder='templates')

@location.route("/location/<api_key>/getAll")
def get_all(api_key):
    company_id = check_company_key(api_key)
    if company_id == None:
        return "API key not valid", 500

    res = all() 
    return res, 200

@location.route("/location/<api_key>/get/<id>")
def get_one(api_key, id):
    company_id = check_company_key(api_key)
    if company_id == None:
        return "API key not valid", 500

    res = one(id)
    if res == None:
        return "Location not found", 404

    return res, 200

@location.route("/location/<api_key>/modify/<id>", methods=["PUT"])
def modify(api_key, id):
    company_id = check_company_key(api_key)
    if company_id == None:
        return "API key not valid", 500

    location_dict = request.json
    res = update(id, **location_dict)
    res['company_id'] = company_id

    return res, 200

@location.route("/location/<api_key>/delete/<id>", methods=["DELETE"])
def remove(api_key, id):
    company_id = check_company_key(api_key)
    if company_id == None:
        return "API key not valid", 500

    count =delete(id)
    if count != 1:
        return "Item not found", 404
    
    return "Item deleted", 200
