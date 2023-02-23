#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):

    def test_FileStorage(self):

        all_objs = storage.all()

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(str(my_model), str(my_model))

    def test_all_FileStorage(self):
        self.assertEqual(storage.all(), storage.all())

    def test_save(self):
        all_objs = storage.all()
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model.save()

        with open('file.json', 'r') as f:
            content = json.load(f)
            key = "{}.{}".format(type(my_model).__name__, my_model.id)
            self.assertEqual(content[key]['name'], my_model.name)

        self.assertEqual(storage.reload(), storage.reload())
        self.assertEqual(storage.all(), storage.all())
