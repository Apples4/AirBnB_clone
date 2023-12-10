#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class Test_Amenity(unittest.TestCase):
    """ unittest for class Amenity"""

    am = Amenity()

    def setUp(self):
        """setting up variables"""
        FileStorage._FileStorage__file_path = "test.json"
        self.am.name = "name"
        self.am.save()

    def test_amenity(self):
        """ testing amenity type"""
        self.assertEqual(type(self.am.name), str)

    def test_subclass(self):
        """ test if Amenity is
        subclass of BaseModel"""
        self.assertTrue(issubclass(self.am.__class__, BaseModel), True)

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
