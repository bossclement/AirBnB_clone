#!/usr/bin/python3
"""User class model"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class definition

    Attrs:
        email (str): email person
        password (str): password string
        first_name (str): first name string
        last_name (str): last name string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
