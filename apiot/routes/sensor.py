from flask import Blueprint

sensor = Blueprint('sensor', __name__, template_folder='templates')

@sensor.route("/sensor/<api_key>/getAll")
def get_all(api_key):
    sensor_id = check_sensor_key(api_key)
    if sensor_id == None:
        return "API key not valid", 500

    res = all()
    return res, 200

@sensor.route("/sensor/<api_key>/get/<id>")
def get_all(api_key, id):
    sensor_id = check_company_key(api_key)
    if sensor_id == None:
        return "API key not valid", 500

    res = one(id)
    if res == None:
        return "Location not found", 404

    return res, 200
    
@sensor.route("/sensor_data/", method=["GET"])
def get_sensor_data():
    pass

@sensor.route("/sensor_data/", method=["POST"])
def post_sensor_data():
    pass

# ----
