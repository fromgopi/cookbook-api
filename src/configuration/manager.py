"""Configuration manager"""
import os
import sys
import logging
from dotenv import load_dotenv, find_dotenv
from src.common.constants import ENV_PATH
from src.common.exceptions import ConfigurationError
import src.resources.strings.configuration as strings

def get_configuration(logger):
    """Loads configuration from .env and aws secrets manager"""
    try:
        def configuration():
            return None
        if not find_dotenv(ENV_PATH):
            raise ConfigurationError(strings.ENV_FILE_NOT_FOUND)
        load_dotenv(ENV_PATH, verbose=True)
        configuration.NAME = os.getenv('NAME')
        # Flask debug + testing
        configuration.DEBUG = (os.getenv('FLASK_DEBUG') == 'True')
        configuration.TESTING = (os.getenv('TESTING') == 'True')
        # Auth
        configuration.AUTH_TOKEN_EXPIRY = os.getenv('AUTH_TOKEN_EXPIRY')
        # Logging
        configuration.LOG_CONSOLE_LEVEL = os.getenv('LOG_CONSOLE_LEVEL')
        configuration.LOG_DEBUG_FILE_LEVEL = os.getenv('LOG_DEBUG_FILE_LEVEL')
        configuration.LOG_DEBUG_FILE_TO = os.getenv('LOG_DEBUG_FILE_TO')
        configuration.LOG_ERROR_FILE_LEVEL = os.getenv('LOG_ERROR_FILE_LEVEL')
        configuration.LOG_ERROR_FILE_TO = os.getenv('LOG_ERROR_FILE_TO')
        configuration.MONGODB_SETTINGS = os.getenv('MONGODB_SETTINGS')
        
        return configuration
    except ConfigurationError as error:
        logger.fatal('[Boot] ' + getattr(error, 'message', str(error)))
        sys.exit(1)

def setup_configuration():
    """Configures the app"""
    logger = logging.getLogger(__name__)
    configuration = get_configuration(logger)