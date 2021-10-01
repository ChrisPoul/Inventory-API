import click
from EnGo.models import db
from flask.cli import with_appcontext


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized database")


def init_db():
    db.drop_all()
    db.create_all()