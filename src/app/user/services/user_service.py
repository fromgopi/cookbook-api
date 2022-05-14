"""User service """
from cmath import log
from http import HTTPStatus as http_status
from src.common import response
import uuid
import logging

class UserService:
    """User service class"""
    
    
    def get_many_users(self):
        users = {
                'id': 10,
                'first_name': 'Gopi Krishna',
                'last_name': 'M'
        }
        return response.success(http_status.OK, resource_name='users', resource_data=users, meta=None)
    
    
    
    
    