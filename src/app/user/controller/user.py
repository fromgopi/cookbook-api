from flask import Blueprint, request
import os
from src.app.user.services.user_service import UserService
import uuid

USER_API = Blueprint('users', __name__)

@USER_API.route('/users', methods=['GET'])
def get_many():
    """Get all the users"""
    try:
        users = UserService().get_many_users()
        
        return {'status': 'ok', 'data': users}
    except (TypeError) as ex:
        print('An exception occurred')




