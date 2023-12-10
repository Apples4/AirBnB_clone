#!/usr/bin/python3
"""
importing depandancies
"""

import os
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected_output = '[BaseModel] ({}) {}'.format(
                                            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()

        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_None(self):
        base1 = BaseModel(None)
        base2 = BaseModel(None)
        self.assertNotEqual(base1.id, base2.id)


class Test_Save(unittest.TestCase):
    """ class to test the save function in BaseModel"""

    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        self.base = BaseModel()
        self.base.save()

    def test_save(self):
        """ test to see if function saves"""
        self.base = BaseModel()
        self.Update = self.base.updated_at
        self.base.save()
        self.assertLess(self.Update, self.base.updated_at)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass


class Test_to_dict(unittest.TestCase):
    """ class to test dict """

    def test_dict(self):
        """ test the dict"""
        date = datetime.now()
        base = BaseModel()
        base.id = "123"
        base.created_at = base.updated_at = date
        dict_1 = {
                "id": "123",
                "created_at": date.isoformat(),
                "updated_at": date.isoformat(),
                "__class__": "BaseModel"
        }
        self.assertDictEqual(base.to_dict(), dict_1)

    def test_type(self):
        """ test the dict type"""
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_attr(self):
        """ test dict attr """
        base = BaseModel()
        base_name = "base"
        base_num = 123
        self.assertNotIn("name", base.to_dict())
        self.assertNotIn("my_number", base.to_dict())


if __name__ == '__main__':
    unittest.main()
