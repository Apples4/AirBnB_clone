#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.user import User
import models
from datetime import datetime
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """test for User class"""

    def setUp(self):
        """setting up the data"""
        FileStorage._FileStorage__file_path = "file.json"

    def test_argsNone(self):
        """Using None as argument"""
        non = User(None)
        self.assertNotIn(None, non.__dict__.values())

    def test_kwargsNone(self):
        """using None as kwargs"""
        non = User(None)
        self.assertIsNotNone(non.id)
        self.assertIsNotNone(non.created_at)
        self.assertIsNotNone(non.updated_at)

    def test_id_BaseModel(self):
        """testing id type"""
        self.assertEqual(str, type(User().id))

    def test_argsNo(self):
        """test with no arguments"""
        self.assertEqual(User, type(User()))

    def test_created_datetime(self):
        """test for created datetime"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_datetime(self):
        """test for updated time"""
        self.assertEqual(datetime, type(User().created_at))

    def test_email(self):
        """test for email attribute"""
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """test the password attribute"""
        self.assertEqual(str, type(User.password))

    def test_firstname(self):
        """test the firstname attribute"""
        self.assertEqual(str, type(User.first_name))

    def test_lastname(self):
        """test the last name attribute"""
        self.assertEqual(str, type(User.last_name))

    def test_id_unique(self):
        """testing if Id is unique"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at(self):
        """Test if created at is works"""
        user1 = User()
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_kwargs(self):
        """testing kwargs input"""
        date1 = datetime.today()
        date2 = date1.isoformat()
        user = User(id="1234", created_at=date2, updated_at=date2)
        self.assertEqual(user.id, "1234")
        self.assertEqual(user.created_at, date1)
        self.assertEqual(user.updated_at, date1)


if __name__ == '__main__':
    unittest.main()
