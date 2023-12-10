#!/usr/bin/python3

"""importing depandancies"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage"""
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        del self.storage
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        self.storage.new(self.model)
        self.assertIn("BaseModel."+self.model.id, self.storage.all())

    def test_save(self):
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel."+self.model.id, f.read())

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel."+self.model.id, self.storage.all())


if __name__ == '__main__':
    unittest.main()
