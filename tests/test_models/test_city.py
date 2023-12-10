#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class Test_City(unittest.TestCase):
    """ unittest for class City"""

    ct = City()

    def setUp(self):
        """setting up variables"""
        FileStorage._FileStorage__file_path = "test_json"
        self.ct.stat_id = "state_id"
        self.ct.name = "name"
        self.ct.save()

    def test_type(self):
        """ class to get the type class attr"""
        self.assertEqual(type(self.ct.name), str)
        self.assertEqual(type(self.ct.state_id), str)

    def test_subclass(self):
        """ test if its a subclass"""
        self.assertTrue(issubclass(self.ct.__class__, BaseModel), True)

    def test_inherit(self):
        """ test to see inherits"""
        self.assertTrue(hasattr(self.ct, "id"))
        self.assertTrue(hasattr(self.ct, "created_at"))
        self.assertTrue(hasattr(self.ct, "updated_at"))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
