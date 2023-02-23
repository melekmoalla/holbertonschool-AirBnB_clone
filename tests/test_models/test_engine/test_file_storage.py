#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):

        all_objs = storage.all()


        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(str(my_model), str(my_model))