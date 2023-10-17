#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import uuid
from datetime import datetime
import sys
import os
import unittest
import json

captured_output = StringIO()
sys.stdout = captured_output
current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class TestBaseModel(unittest.TestCase):
    def test_create_base_model(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertIn("__class__", my_model_json)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertIn("id", my_model_json)
        self.assertIn("created_at", my_model_json)
        self.assertIn("updated_at", my_model_json)
        self.assertIn("name", my_model_json)
        self.assertIn("my_number", my_model_json)

    def test_from_dict(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)

if __name__ == '__main__':
    unittest.main()
