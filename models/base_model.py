#!/usr/bin/python3
""" importing depancies"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """initalizzing the base model"""

    def __init__(self, *args, **kwargs):
        """
        init function
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if isinstance(val, str):
                        val = datetime.strptime(
                                        val,
                                        '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of class data"""
        return("[{}] ({}) {}".format(
                            self.__class__.__name__,
                            self.id,
                            self.__dict__))

    def save(self):
        """
        function to update_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Add the __class__ key with the class name of the object
        Returns: a dictionary containing all keys/values of object
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        """
        Convert 'created_at' and 'updated_at'
        to string object in ISO format
        """
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
