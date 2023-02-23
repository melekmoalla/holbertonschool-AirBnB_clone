#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class testBase_AirBnB(unittest.TestCase):

    def test_to_dict(self):
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
            str(my_model_json), "{'my_number': 89, 'name': 'My First Model', 'updated_at': '2023-02-23T19: 56: 31.436968', 'id': 'e23b2f5d-725e-499f-ba35-90af20ec966b', 'created_at': '2023-02-23T19: 56: 31.436876', '__class__': 'BaseModel'}")
        print(my_model_json)

    def test_str(self):
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)
