from apiot.db import get_db
from pypika import Table, Query
from itertools import cycle

location = Table("location")

modify_schema = {
    "type": "object",
    "properties": {
        "location_name":    {"type": "string"},
        "location_country": {"type": "string"},
        "location_city":    {"type": "string"},
        "location_meta":    {"type": "string"},
    },
}

def one(id):
    q = Query.from_(location).select('*').where(location.id == id)
    res = get_db().cursor().execute(q.get_sql())

    if (row := res.fetchone()) == None:
        return None

    return { i: j for i,j in zip([x[0] for x in res.description], row) }

def all(company_id):
    q = Query.from_(location).select('*').where(location.company_id == company_id)
    print(q)
    res = get_db().cursor().execute(q.get_sql())
    print(res.rowcount)

    return [ {j:k for j, k in zip([x[0] for x in res.description], i)} for i in res.fetchall() ]


def update(id, **fields):
    q = Query.update(location)\
            .set(location.location_name, fields["location_name"])\
            .set(location.location_country, fields["location_country"])\
            .set(location.location_city, fields["location_city"])\
            .set(location.location_meta, fields["location_meta"])\
            .where(location.id == id)
    res = get_db().cursor().execute(q.get_sql())

    if res.rowcount == 0:
        q = Query.into(location)\
                .columns(*fields.keys())\
                .insert(*fields.values())
        res = get_db().cursor().execute(q.get_sql())
    get_db().commit()

    fields['id'] = int(id)
    return fields

def delete(id):
    q = Query.from_(location).where(location.id == id).delete()
    res = get_db().cursor().execute(q.get_sql())

    get_db().commit()
    return res.rowcount


