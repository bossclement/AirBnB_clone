#!/usr/bin/python3
"""City class model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class definition
    Attrs:
        state_id (str): foreign key identity
        name (str): city name
    """
    state_id = ""
    name = ""
