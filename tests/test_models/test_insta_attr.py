#!/usr/bin/python3
""" importing depancies"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class TestSubclass(unittest.TestCase):
    """Test for subclass attributes"""

    def setUp(self):
        """set up for the test"""
        self.user = User()
        self.city = City()
        self.place = Place()
        self.review = Review()
        self.amenity = Amenity()
        self.state = State()

    def test_user(self):
        """ Test for user"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_city(self):
        """ Test for city class"""
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_place(self):
        """ Test for place class"""
        self.assertIsInstance(self.place, Place)
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_review(self):
        """Test the review class"""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_amenity(self):
        """Test the amenty class"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_state(self):
        """ test state class"""
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "name"))


if __name__ == '__main__':
    unittest.main()
