from flask import current_app, g
from pypika import Table, Query
import sqlite3


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])

    return g.db

def close_db(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

