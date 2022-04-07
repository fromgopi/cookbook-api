from flask import Blueprint, request
import os
from src.app.user.services.user_service import UserService

USER_API = Blueprint('users', __name__)

@USER_API.route('/users', methods=['GET'])
def get_many():
    """Get all the users"""
    try:
        data = UserService.get_many()
        print(data)
        return 'ok'
    except (TypeError) as ex:
        print('An exception occurred')
