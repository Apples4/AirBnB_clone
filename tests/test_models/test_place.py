#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.place import Place
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class Test_Place(unittest.TestCase):
    """Class to test the Place class"""

    pc = Place()

    def setUp(self):
        FileStorage._FileStorage__filepath = "test_json"
        self.pc.city_id = "city is"
        self.pc.user_id = "user id"
        self.pc.name = "name"
        self.pc.description = "description"
        self.pc.number_rooms = 1
        self.pc.number_bathrooms = 1
        self.max_guest = 1
        self.pc.price_by_night = 1
        self.pc.latitude = 1.1
        self.pc.longitude = 1.1
        self.pc.amenity_ids = "amenity_ids"
        self.pc.save()

    def test_type(self):
        """ test the types for attributes"""
        self.assertEqual(type(self.pc.city_id), str)
        self.assertEqual(type(self.pc.user_id), str)
        self.assertEqual(type(self.pc.name), str)
        self.assertEqual(type(self.pc.description), str)
        self.assertEqual(type(self.pc.number_rooms), int)
        self.assertEqual(type(self.pc.number_bathrooms), int)
        self.assertEqual(type(self.pc.max_guest), int)
        self.assertEqual(type(self.pc.price_by_night), int)
        self.assertEqual(type(self.pc.latitude), float)
        self.assertEqual(type(self.pc.longitude), float)
        self.assertEqual(type(self.pc.amenity_ids), str)

    def test_IfSubclass(self):
        """ test if place is a subclass """
        self.assertTrue(issubclass(self.pc.__class__, BaseModel), True)

    def test_inherit(self):
        """ test if it inherts from superclass"""
        self.assertTrue(hasattr(self.pc, "id"))
        self.assertTrue(hasattr(self.pc, "created_at"))
        self.assertTrue(hasattr(self.pc, "updated_at"))

    def tearDown(self):
        """ removes files for test"""
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
