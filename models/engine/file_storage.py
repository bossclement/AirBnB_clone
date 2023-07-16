#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Handles serialization and deserialization of classes
    Attr:
        file_path (str): path to the JSON file
        objects (dict): storing objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __object with key"""
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        FileStorage.__objects[f"{obj_name}.{obj_id}"] = obj
