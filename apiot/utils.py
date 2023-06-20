from pypika import Tables, Query
from apiot.db import get_db
from hashlib import sha256
import time
import os

company, sensor = Tables('Company', 'Sensor')

def generate_key(name):
    key = os.urandom(16)
    key += name.encode()[:16] if len(name) > 15 else name.encode() + os.urandom(16 - len(name))

    return sha256(key).hexdigest()[:10]

def check_company_key(key):
    q = Query.from_(company).select('id').where(company.company_api_key == key)
    res = get_db().cursor().execute(q.get_sql()).fetchall()

    if len(res) == 1:
        return res[0][0]
    return None

def check_sensor_key(key):
    q = Query.from_(sensor).select('id').where(sensor.sensor_api_key == key)
    res = get_db().cursor().execute(q.get_sql()).fetchall()

    if len(res) == 1:
        return res[0][0]
    return None

