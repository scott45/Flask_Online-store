from flask import flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy(app)


def create_app(config_name):
    '''
    creates a Flask instance in __init__.py file of my package
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
