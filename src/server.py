from flask import Flask
from flask_restful import Api


API = Api()

def create_app():
    app = Flask(__name__)
    API.init_app(app)
    