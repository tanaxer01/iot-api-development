from flask import Blueprint, request, jsonify
from apiot.models.company import *

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route("/admin/createCompany", methods=["POST"])
@expects_json(create_schema)
def create():
    company_dict = request.json

    res = create_company(**company_dict)
    return res, 201
