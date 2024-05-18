#!/usr/bin/python3
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from models.engine.file_storage import FileStorage
"""
we are gonna test the file_storage file
"""


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """set up the resources for the bloody thing"""
        self.storage = FileStorage()

    def tearDown(self):
        """wibes everything out after we finish"""
        del self.storage

    def test__init__(self):
        """testst the __init__ method"""
        self.assertIsInstance(self.storage.__file_path, str)
        self.assertIsInstance(__objects, dict)
