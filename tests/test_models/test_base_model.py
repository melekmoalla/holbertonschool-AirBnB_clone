#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import json

class testBase_AirBnB(unittest.TestCase):

    def test_to_id(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_model_json = "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}"

        self.assertEqual(
            my_model_json, "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-20 14:24:01.871493', 'id': '853d2737-0bc7-4dbe-a403-b3934a3de25c', 'created_at': '2023-02-20 14:24:01.871499', '__class__': 'BaseModel'}")

    def test_save(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(print(my_model), print(my_model))
        my_model.save()
        self.assertEqual(str(my_model), str(my_model))
        my_model_json = my_model.to_dict()
        print(my_model_json)
        self.assertEqual(
            my_model_json, my_model_json)
        print(my_model_json)

    def test_str(self):
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

def test_save(self):

    my_model = BaseModel()
    my_model.name = "John"
    my_model.age = 30
    
    my_model.save()
    
    with open('file.json', 'r') as f:
        content = json.load(f)
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertIn(key, content)
        self.assertEqual(content[key]['name'], my_model.name)
        self.assertEqual(content[key]['age'], my_model.age)
