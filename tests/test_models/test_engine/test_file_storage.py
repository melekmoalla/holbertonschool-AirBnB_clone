#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_FileStorage(self):

        all_objs = storage.all()

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(str(my_model), "My_First_Model")

    def test_all_FileStorage(self):
        self.assertEqual(storage.all(), storage.all())
