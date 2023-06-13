from flask import current_app, g
import sqlite3
import click

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])

    return g.db

def close_db(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    with current_app.open_resource('schema.sql') as f:
        get_db().executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database')

@click.command('create-admin')
@click.argument('username')
@click.argument('password')
def add_admin_command(username: str, password: str):
    try:
        res = get_db().cursor().execute(f"INSERT INTO Admin (username, password) VALUES ('{username}', '{password}')") 
    except sqlite3.IntegrityError:
        click.echo("User already exists")
        return
    click.echo(f"User {username} created")


def init_app(app):
    """Clear the existing data and create new tables."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_admin_command)


