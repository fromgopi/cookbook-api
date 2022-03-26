from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

API = Api()
DB = MongoEngine()

def create_app():
    app = Flask(__name__)
    API.init_app(app)
    
    