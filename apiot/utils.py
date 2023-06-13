from pypika import Table, Query
from apiot.db import get_db
from hashlib import sha256
import time
import os

def generate_key(name):
    key = os.urandom(16)
    key += name.encode()[:16] if len(name) > 15 else name.encode() + os.urandom(16 - len(name))

    return sha256(key).hexdigest()[:10]

# middleware
def check_key(key):
    company = Table("company")
    sensor  = Table("sensor")

    query1 = Query().from_(company).select(company.id).where(company.api_key == key)
    res = get_db().cursor().execute(str(query1))

    rows = res.fetchall()
    if len(rows) == 1:
        return rows[0]


    query2 = Query().from_(sensor).select(sensor.id).where(sensor.api_key == key)
    res = get_db().cursor().execute(str(query2))

    if len(res.fetchall()) == 1:
        return True

    return False

                 

