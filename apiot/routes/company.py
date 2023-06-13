from flask import Blueprint, request, jsonify
from apiot.models.company import *
from apiot.bcrypt import get_bcrypt, get_secret

company = Blueprint('company', __name__, template_folder='templates')

@company.route("/company", methods=["POST"])
@expects_json(create_scheme)
def create():
    company_dict = request.json
    company_dict["api_key"] = get_bcrypt().generate_password_hash(company_dict["name"]+get_secret()).decode("utf-8")

    res = create_company(**company_dict)
    return company_dict, 201

#@company.route("/company", methods=["GET"])
#def get_all(id: int):
#    if res := one(id):
#        return res, 200
#    return "", 404

@company.route("/company/<id>", methods=["GET"])
def get_one(id: int):
    if res := one(id):
        return res, 200
    return "", 404

@company.route("/company", methods=["UPDATE"])
def update():

    return "test"

@company.route("/company", methods=["DELETE"])
def delete():
    return "test"


