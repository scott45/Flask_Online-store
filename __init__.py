from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from .auth import auth as auth_blueprint

db = SQLAlchemy()

"""
Flask-Login provides user session management for Flask.
It handles the common tasks of logging in, logging out,
and remembering your users’ sessions over extended periods of time.
"""
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    '''
    creates a Flask instance in __init__.py file of my package
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    db.init_app(app)
    login_manager.init_app(app)
    return app
