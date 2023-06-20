from pypika import Table, Tables, Query
from apiot.db import get_db, close_db
from apiot.models.sensor import create_sensor
from hashlib import sha256
import click
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


@click.command('init-db')
def init_db_command():
    with current_app.open_resource('schema.sql') as f:
        get_db().executescript(f.read().decode('utf8'))

    click.echo('Initialized the database')

@click.command('create-admin')
@click.argument('username')
@click.argument('password')
def add_admin_command(username: str, password: str):
    admin = Table('Admin')

    q = Query.into(admin).insert(username,password)
    res = get_db().cursor().execute(q.get_sql())
    get_db().commit()

    click.echo(f"User {username} created")

@click.command('create-sensor')
@click.argument('loc_id')
@click.argument('name')
@click.argument('country')
@click.argument('city')
@click.argument('meta')
def add_sensor_command(loc_id: int, name: str, country: str, city: str, meta: str):
    sensor = Table('Sensor')

    api_key = generate_key("".join([loc_id, name, country, city, meta]))
    res = create_sensor(loc_id, name, country, city, meta, api_key)

    if res:
        click.echo(f"Sensor {name} created, api_key: {api_key}")

def init_app(app):
    """Clear the existing data and create new tables."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_sensor_command)
    app.cli.add_command(add_admin_command)



