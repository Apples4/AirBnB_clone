#!/usr/bin/python3
import json
import os.path
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
        FSobj_dict = FileStorage.__objects
        obj_name = obj.__class__.__name__
        FSobj_dict["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """
        function that serialises to JSON file
        """
        FSobj_dict = FileStorage.__objects
        obj_dict = {obj: FSobj_dict[obj].to_dict()
                    for obj in FSobj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileSotrage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_d)(**obj))
            return
