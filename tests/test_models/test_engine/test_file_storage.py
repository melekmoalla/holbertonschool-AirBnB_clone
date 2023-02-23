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
        my_model.name = "John"
        
        my_model.save()
        all_objs = storage.all()

        with open('file.json', 'r') as f:
            content = json.load(f)
            key = "{}.{}".format(type(my_model).__name__, my_model.id)
            self.assertEqual(content[key]['name'], my_model.name)
            self.assertEqual(all_objs , all_objs)
            

    def test_filestorage_all(self):
            storage = FileStorage()
            obj1 = BaseModel()
            obj1.save()
            obj2 = BaseModel()
            obj2.save()
            obj3 = BaseModel()
            obj3.save()
            all_objs = storage.all()
            self.assertEqual(all_objs , all_objs)
