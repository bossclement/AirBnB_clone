#!/usr/bin/python3
"""
This module contains a class which is used as a base model
of all the other classes used in this project
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base model class for the whole project
    """

    def __init__(self):
        """
        Constructor function for base model class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representaion of the instance of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the update_at variable to the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/value pairs
        of __dict__ of the instance of this class.
        """
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data