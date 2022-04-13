""" Development task runner"""
import os 
from logging import getLogger
from unittest import main
from flask_script import Manager
from src.common.constants import DEFAULT_PORT  
  
from src.configuration.modules.logger import RequestHandlerLoggerOverride 

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
    port = int(port) if port else DEFAULT_PORT
    
    APP.run(
        host='0.0.0.0',
        port=port,
        debug=enable_debug,
        use_reloader=enable_debug,
        threaded=True,
        request_handler=RequestHandlerLoggerOverride
    )
    
if __name__ == '__main__':
    MANAGER.run()
