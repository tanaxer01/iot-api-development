from flask_expects_json import expects_json
from pypika import Table, Query
from apiot.utils import generate_key
from apiot.db import get_db

company = Table("Company")

create_scheme = {
    "type": "object",
    "properties": { "company_name": {"type": "string"}, },
    "required": ["company_name"]
}

def create_company(**company_dict):
    company_dict["api_key"] = generate_key("".join(company_dict.values()))

    query = Query().into(company).columns("name", "api_key").insert(*list(company_dict.values()))
    res = get_db().cursor().execute(str(query))
    get_db().commit()

    return company_dict


# READ
def one(id: int):
    query = Query().from_(company).select(company.id, company.name, company.city, company.meta).where(company.id == id)
    res = get_db().cursor().execute(str(query))

    return res.fetchone()

def all(id: int, name: str, city: str, meta: str):
    pass

# UPDATE
def update_company(id: int, name: str, city: str, meta: str):
    #query = Query().update(company).
    pass

def delete_company(id: int, name: str, city: str, meta: str):
    pass
