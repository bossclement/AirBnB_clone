
#!/usr/bin/python3
"""
This module has a class that serializes instances to a
JSON file and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    The class the serializes instances of a class
    and deserializes them from a JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all the instances stored.
        """
        return self.__objects
    
    def new(self, obj):
        """
        Inserts a new object to my list of objects stored
        :param obj: The object to insert
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        Save the objects to a file by converting the dictionary
        object to a JSON string.
        """
        data = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """
        deserializes JSON string to a python dictionary
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for obj in json.load(file).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass

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

