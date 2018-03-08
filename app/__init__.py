import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    """
    Creates the flask application, registers it with Bootstrap, initializes it and sets up flask blueprints.
    Also initializes database tables.
    """
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.secret_key = 'a super secret key'
    
    Bootstrap(app)
    with app.app_context():
        db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models
    with app.app_context():
        db.create_all()
    
    migrate = Migrate(app, db)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
