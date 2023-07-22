#!/usr/bin/python3
"""
This module contains a class which is used as a base model
of all the other classes used in this project
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base model class for the whole project
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor function for base model class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Overwrite the attribute's values to new ones
        if kwargs:
            for attr, value in kwargs.items():
                if attr in ["created_at", "updated_at"]:  # change to datetime
                    setattr(self, attr, datetime.fromisoformat(value))
                elif attr != "__class__":  # Ignore the __class__ value
                    setattr(self, attr, value)
        else:
            models.storage.new(self)  # pass in the instance of the class

    def __str__(self):
        """
        Returns string representaion of the instance of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the update_at variable to the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
