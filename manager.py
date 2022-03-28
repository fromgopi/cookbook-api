""" Development task runner"""
import os
from logging import getLogger
from flask_script import Manager

from src.server import create_app

APP = create_app()
APP.app_context().push()

MANAGER = Manager()

LOGGER = getLogger(__name__)

@MANAGER.command
def run():
    """Development Init"""
    port = os.getenv('PORT')
    enable_debug = (os.getenv('FLASK_DEBUG') == 'True')