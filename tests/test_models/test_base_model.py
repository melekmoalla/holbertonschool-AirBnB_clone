#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(print(my_model_json), None)
