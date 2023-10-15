#!/usr/bin/python3

"""define unittest for user class"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """test user class"""
    def setUp(self):
        """setUp user"""
        self.user = User()

    def tearDown(self):
        """delete user"""
        del self.user

    def test_empty_attributes(self):
        """test_empty_attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.assertTrue(issubclass(User, BaseModel))

    def test_attribute_assignment(self):
        """assign the attributes"""
        email_value = "test@gmail.com"
        self.user.email = email_value
        password_value = "aabbccddee"
        self.user.password = password_value
        first_name_val = "abcd"
        self.user.first_name = first_name_val
        last_name_value = "efgh"
        self.user.last_name = last_name_value

        self.assertEqual(self.user.email, email_value)
        self.assertEqual(self.user.password, password_value)
        self.assertEqual(self.user.first_name, first_name_val)
        self.assertEqual(self.user.last_name, last_name_value)


if __name__ == '__main__':
    unittest.main()
