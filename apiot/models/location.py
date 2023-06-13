from pypika import Table, Query
from apiot.db import get_db

location = Table("location")

modify_scheme = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "country": {"type": "string"},
        "city": {"type": "string"},
        "meta": {"type": "string"},
    },
}

def one(id: int):
    query = Query().from_(location).select(location.id, location.name, location.country, location.city, location.meta).where(location.id == id)
    res = get_db().cursor().execute(str(query))

    return res.fetchone()

def all():
    query = Query().from_(location).select(location.id, location.name, location.country, location.city, location.meta)
    res = get_db().cursor().execute(str(query))

    return res.fetchall()

def update(id, **fields):
    query = Query().into(location)\
            .columns("name", "city", "country", "meta")\
            .insert(*list(fields.values()))
            .on_duplicate_key_update(
    res = get_db().cursor().execute(str(query))
    get_db().commit()

    fields["id"] = id
    return fields




