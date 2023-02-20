#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class testBase_AirBnB(unittest.TestCase):

    def test_save(self):
        model = BaseModel()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json, my_model_json)

    def test_BaseModel_id(self):
        my_model = BaseModel()
        self.assertEqual(my_model.id, my_model.id)

    def test_self_created_at(self):
        my_model = BaseModel()
        self.assertEqual(my_model.created_at, my_model.created_at)

    def test_str(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        a = print(my_model)
        self.assertEqual(a, a)
