#!/usr/bin/python3

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):


    def test_save(self):
        my_model = BaseModel()
        my_model.name = "John"

        my_model.save()

        with open('file.json', 'r') as f:
            content = json.load(f)
            key = "{}.{}".format(type(my_model).__name__, my_model.id)
            self.assertEqual(content[key]['name'], my_model.name)


