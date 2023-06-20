from flask_expects_json import expects_json
from pypika import Table, Query
from apiot.db import get_db
from apiot.utils import generate_key

company = Table('Company')

create_schema = {
    "type": "object",
    "properties": { "company_name": {"type": "string"} },
    "required": ["company_name"]
}

def create_company(**company_dict):
    company_dict['company_api_key'] = generate_key("".join(company_dict.values()))

    q = Query.into(company)\
            .columns('company_name', 'company_api_key')\
            .insert(company_dict['company_name'], company_dict['company_api_key'])
    res = get_db().cursor().execute(q.get_sql())
    get_db().commit()

    return company_dict
