"""User Model"""
from src.server import DB


class User(DB.Document):
    first_name = DB.StringField(required=True, max_length=50)
    last_name = DB.StringField(required=True, max_length=50)
    email = DB.StringField(required=True, max_length=50)