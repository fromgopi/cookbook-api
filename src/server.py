import os
import sys
from click import option
from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from src.app.user.controller.user import USER_API
from src.common.error_handler import get_traceback
from src.configuration.modules.logger import setup_logger
from src.configuration.manager import setup_configuration


API = Api()
DB = MongoEngine()

def create_app():
    try:
        app = Flask(__name__)
        API.init_app(app)
        setup_configuration(app)
        setup_logger(app.config)
        DB.init_app(app)
        register_blueprints(app)
        return app
    except (Exception) as ex:
        print(ex)
        sys.exit(1)


def register_blueprints(app):
    """Register Blueprints"""
    from src.app.user.controller.user import USER_API
    app.register_blueprint(USER_API, url_prefix=os.getenv('ROUTE_PREFIX'))
    
    
    
    
    
    
