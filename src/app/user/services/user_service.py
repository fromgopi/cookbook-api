"""User service """
from cmath import log
from http import HTTPStatus as http_status
from src.common import response
import uuid
import logging

class UserService:
    """User service class"""
    def __init__(self) -> None:
        self.log = logging.getLoggerClass(__class__)
    
    def get_many(self):
        try:
            users = {
                'id': uuid.uuid5(),
                'first_name': 'Gopi Krishna',
                'last_name': 'M'
            }
            print(self.log)
            return users
        except (TypeError) as ex:
            print(ex)
            
            
            
            
            
            