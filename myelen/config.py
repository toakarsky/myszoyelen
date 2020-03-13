import os


class Config:
    SECRET_KEY = 'SECRET_KEY'


class DevConfig:
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
