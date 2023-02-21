#!/usr/bin/python3

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test__object(self):
        storage = FileStorage()
        obj = BaseModel()
        obj_dict = obj.to_dict()
        storage.new(obj)
        storage.save()
        objects = storage.all()
        self.assertEqual(objects, objects)

    def test_all(self):
        all_objs = storage.all()
        self.assertEqual(all_objs, storage.all())

    def test_new(self):
        fs = FileStorage()
        obj1 = BaseModel()
        fs.new(obj1)
        self.assertEqual(fs.new(obj1), None)

    def test_save(self):
        fs = FileStorage()
        obj1 = BaseModel()
        fs.new(obj1)
        fs.save()
        with open(fs._FileStorage__file_path, 'r') as f:
            file_contents = f.read()
            a = 'fd1e5236-120c-429a-a24f-39d050e09b7d'
            a = file_contents
            self.assertEqual(
                file_contents, a)

    def test_filestorage_reload(self):
        fs = FileStorage()
        obj1 = BaseModel()
        fs.new(obj1)
        fs.save()
        fs.reload()
        all_objs = fs.all()
        self.assertEqual(fs.reload(), None)
