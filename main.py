import os
from src.common.constants import DEFAULT_PORT
from src.configuration.modules.logger import RequestHandlerLoggerOverride
from src.server import create_app

def create_instance():
    """Development Init"""
    app = create_app() 
    port = os.getenv('PORT') 
    enable_debug = (os.getenv('FLASK_DEBUG') == 'True')
    port = int(port) if port else DEFAULT_PORT 
    app.run(
        host='0.0.0.0',
        port=port,
        debug=enable_debug,
        use_reloader=enable_debug,
        threaded=True,
        request_handler=RequestHandlerLoggerOverride
    )
    

if __name__ == '__main__':
    create_instance()
    
    
