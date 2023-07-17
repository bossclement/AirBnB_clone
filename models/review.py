#!/usr/bin/python3
"""Review class model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition
    Attrs:
        place_id (str): foreign key id
        user_id (str): foreign key id
        text (str): a body of paragraph
    """
    place_id = ""
    user_id = ""
    text = ""
