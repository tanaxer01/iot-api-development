from apiot.db import get_db
from pypika import Table, Query

sensor = Table("sensor")

modify_schema = {
    "type": "object",
    "properties": {
        "sensor_name":    {"type": "string"},
        "sensor_country": {"type": "string"},
        "sensor_city":    {"type": "string"},
        "sensor_meta":    {"type": "string"},
    },
}

def create_sensor(loc_id: int, name: str, country: str, city: str, meta: str, api_key: str):
    q = Query.into(sensor)\
            .columns('location_id', 'sensor_name', 'sensor_country', 'sensor_city', 'sensor_meta', 'sensor_api_key')\
            .insert(loc_id, name, country, city, meta, api_key)
    res = get_db().cursor().execute(q.get_sql())
    get_db().commit()

    return True


def one(id):
    q = Query.from_(sensor).select('*').where(sensor.id == id)
    res = get_db().cursor().execute(q.get_sql())

    if (row := res.fetchone()) == None:
        return None

    return { i: j for i,j in zip([x[0] for x in res.description], row) }

def all(api_key):
    q = Query.from_(sensor).select('*').where(sensor.sensor_api_key == api_key)
    res = get_db().cursor().execute(q.get_sql())

    return [ {j:k for j, k in zip([x[0] for x in res.description], i)} for i in res.fetchall() ]


