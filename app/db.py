import sqlite3
from flask import g, current_app


import click


def connect_db():
    rv = sqlite3.connect(current_app.config['DATABASE'])
    return rv


def get_db():
    if not hasattr(g, 'flaskr.db'):
        g.sqlite_db = connect_db()
        g.row_factory = sqlite3.Row
    return g.sqlite_db


def init_db():
    with current_app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# @app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'flaskr.db'):
        g.sqlite_db.close()


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Database initialized and populated')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
