#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.state import State
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class Test_State(unittest.TestCase):
    """unittest for class State"""
    st = State()

    def setUp(self):
        """setting up variables"""
        FileStorage._FileStorage__file_path = "test_json"
        self.st = State()
        self.st.name = "name"
        self.st.save()

    def test_str(self):
        """test attribute str """
        self.assertEqual(type(self.st.name), str)

    def test_subclass(self):
        """Test if state is subclass"""
        self.assertTrue(issubclass(self.st.__class__, BaseModel), True)
        self.assertIsInstance(self.st, State)

    def test_attr(self):
        """test the if it has attribute"""
        self.assertTrue(hasattr(self.st, "name"))

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
