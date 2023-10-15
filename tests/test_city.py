#!/usr/bin/python3

"""define city class"""

import unittest
from models.city import City
from models.state import State
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """city classs"""
    def setUp(self):
        """setup city"""
        self.state = State()
        self.city = City()

    def tearDown(self):
        """delete city"""
        del self.city

    def test_empty_attributes(self):
        """test empty attr"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attribute_assignment(self):
        """assign attr"""
        state_id_value = self.state.id
        self.city.state_id = state_id_value
        name_value = "Rabat"
        self.city.name = name_value

        self.assertEqual(self.city.state_id, state_id_value)
        self.assertEqual(self.city.name, name_value)

    def test_inheritance(self):
        self.assertTrue(issubclass(City, BaseModel))

if __name__ == '__main__':
    unittest.main()
