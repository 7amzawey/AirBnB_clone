#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
"""this file is for testing all the different cases and methods of the Airbnb project"""


class TestBaseModel(unittest.TestCase):
    """testing the base model object"""
    def setUp(self):
        """this method sets up the resources for the needed tests"""
        self.model = BaseModel()

    def tearDown(self):
        """cleans up after tests"""
        del self.model

    def test_id(self):
        """"Test that id is correctly assinged and is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test that created time has already been assigned and is a date
        time object"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test that updated at is already implemented and is a datetime
        object"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save(self):
        """Test that save method updated the updated_at attribut"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test that to_dict method displays the info correctly"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_init_kwargs(self):
        """test that test_init_method"""
        data = {'__name__': "moe's test",
                'created_at': '2022-01-01T12:00:00.000000',
                'updated_at': '2022-01-01T12:00:00.000000',
                'id': '5420'}
        model = BaseModel(**data)
        self.assertEqual(model.id, '5420')
        self.assertEqual(model.created_at, datetime.datetime.strptime(data['created_at'],
            "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model.updated_at, datetime.datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))

    def test_init_args(self):
        """test that __init_args methdod"""
        model = BaseModel('arg1', 'arg2', 'arg3')
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.updated_at, datetime.datetime)
        self.assertIsInstance(model.created_at, datetime.datetime)

    def test__str__(self):
        """Test the __str__ method"""
        model_rep = str(self.model)
        string_rep = '[{}] ({}) {}'.format(self.model.__class__.__name__,
                self.model.id,
                self.model.__dict__)
        self.assertEqual(model_rep, string_rep)
