#!/usr/bin/python3
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
"""
we are gonna test the file_storage file
"""


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """set up the resources for the bloody thing"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """wibes everything out after we finish"""
        del self.storage
        del self.model

    def test__init__(self):
        """testst the __init__ method"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """tests the all method"""
        self.assertEqual(
                self.storage.all(),
                self.storage._FileStorage__objects)

    def test_new(self):
        """tests the new method """
        obj = self.model
        self.storage.new(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save(self):
        """test the save method"""
        obj = self.model
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertEqual(data[key], obj.to_dict())

    def test_reload(self):
        """test the reload method"""
        obj = self.model
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        loaded_model = self.storage._FileStorage__objects[key]
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, self.model.id)
        self.assertEqual(loaded_model.created_at, self.model.created_at)
        self.assertEqual(loaded_model.updated_at, self.model.updated_at)
