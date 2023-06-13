from flask_expects_json import expects_json
from pypika import Table, Query
from apiot.db import get_db

admin = Table("")

create_scheme = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"]
}

