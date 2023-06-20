from flask import Blueprint
from apiot.models.sensor import *
from apiot.utils import check_sensor_key

sensor = Blueprint('sensor', __name__, template_folder='templates')

@sensor.route("/sensor/<api_key>/getAll")
def get_all(api_key):
    sensor_id = check_sensor_key(api_key)
    if sensor_id == None:
        return "API key not valid", 500

    res = all(api_key)
    return res, 200

@sensor.route("/sensor/<api_key>/get/<id>")
def get_one(api_key, id):
    sensor_id = check_sensor_key(api_key)
    if sensor_id == None:
        return "API key not valid", 500

    res = one(id)
    if res == None:
        return "Location not found", 404

    return res, 200
    
@sensor.route("/sensor_data/", methods=["GET"])
def get_sensor_data():
    pass

@sensor.route("/sensor_data/", methods=["POST"])
def post_sensor_data():
    pass
