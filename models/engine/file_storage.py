#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """
    Class that serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        function returns the dictionary

        Return:
            returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets dictionary
        The key is a combination of the
        class name and id of the object

        Params:
        obj - key and value for dict
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        function that serialises to JSON file
        """
        my_dict = {}
        my_dict = {key: val.to_dict() for key,
                   val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
            for key, val in objs.items():
                class_name = val.get('__class__')
                obj = eval(class_name + '(**val)')
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
