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

    def save(self):
        """Serialize __objects to the JSON file"""
        objs = FileStorage.__objects
        obj_dict = {key: value for key, value in objs.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects
        Only if JSON file exits
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)

        except FileNotFoundError:
            return
