from pprint import pprint
from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from src.configuration.modules.logger import setup_logger
from src.configuration.manager import setup_configuration

API = Api()
DB = MongoEngine()

def create_app():
    app = Flask(__name__)
    API.init_app(app)
    setup_configuration(app)
    setup_logger(app.config)
    DB.init_app(app)
    return app
