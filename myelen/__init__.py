import os

from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate

from myelen.auth.blueprint import bp as auth_bp

from myelen.database import db
from myelen.config import DevConfig


load_dotenv()

# app
app = Flask(__name__, instance_relative_config=False)
app.config.from_object(DevConfig)

# Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

# DB
db.init_app(app)

# Migrations
migrate = Migrate(app, db)
