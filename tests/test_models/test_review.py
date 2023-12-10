#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.review import Review
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class Test_review(unittest.TestCase):
    """test for Review class"""

    re = Review()

    def setUp(self):
        """setting up variables"""
        FileStorage._FileStorage__file_path = "test.json"
        self.rev = Review()
        self.rev.place_id = "123"
        self.rev.user_id = "123"
        self.rev.text = "123"
        self.rev.save()

    def test_StrType(self):
        """testing str attr"""
        self.assertEqual(type(self.re.place_id), str)
        self.assertEqual(type(self.re.user_id), str)
        self.assertEqual(type(self.re.text), str)

    def test_hasattr(self):
        """ test if there are attributes"""
        self.assertEqual(hasattr(self.re, "place_id"), True)
        self.assertEqual(hasattr(self.re, "user_id"), True)
        self.assertEqual(hasattr(self.re, "text"), True)

    def test_subclass(self):
        """ test if Review is
        subclass of BaseModel"""
        self.assertTrue(issubclass(self.re.__class__, BaseModel), True)
        self.assertIsInstance(self.re, Review)

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
