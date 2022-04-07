"""User service """
from http import HTTPStatus as http_status
from src.common import response
import uuid

class UserService:
    """User service class"""
    
    def get_many(self):
        users = {
            'id': uuid.uuid5(),
            'first_name': 'Gopi Krishna',
            'last_name': 'M'
        }
        return response.success(http_status.ok, 'users', resource_data=users, meta=None)