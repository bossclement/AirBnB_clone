#!/usr/bin/python3
"""Place class model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class definition
    Attrs:
        city_id (str): foreign key id
        user_id (str): foreign key id
        name (str): place name
        description (str): a paragraph telling us info about the place
        number_rooms (int): a number to specify number of rooms a place has
        number_bathrooms (int): a number specifying the number of bathrooms
        max_guest (int): a number to specify maximum number of guests
        price_by_night (int): how much the charge for a night stay
        latitude (float): latitude number
        longitude (float): longitude number
        amenity_ids (list): list of strings for id of amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
