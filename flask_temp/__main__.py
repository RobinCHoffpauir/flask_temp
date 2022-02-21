import click
from flask.cli import FlaskGroup
from flask import *
from . import create_app_wsgi


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script for the flask_temp application."""


if __name__ == "__main__":  # pragma: no cover
    main()

@app.route('/')
def home():  
    return "hello, this is our first flask website";
    if __name__ =='__main__':  
app.run(debug = True)