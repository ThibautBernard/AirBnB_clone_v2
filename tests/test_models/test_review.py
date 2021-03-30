#!/usr/bin/python3
""" """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.review import Review
import os.path
from os import path
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import MySQLdb


class TestReview(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type_place_id(self):
        """ Test type"""
        obj = Review()
        obj.place_id = "dzdz"
        n = getattr(obj, "place_id")
        self.assertIsInstance(n, str)

    def test_type_user_id(self):
        """ Test type"""
        obj = Review()
        obj.user_id = "dzdz"
        n = getattr(obj, "user_id")
        self.assertIsInstance(n, str)

    def test_type_text(self):
        """ Test type"""
        obj = Review()
        obj.text = "dzdzzdz"
        n = getattr(obj, "text")
        self.assertIsInstance(n, str)

    """Basic instanciation object__init__"""
    def test_Review_id_created(self):
        """ Test id created """
        obj = Review()
        self.assertTrue(obj.id is not None)
        self.assertTrue(type(obj) is Review)

    def test_Review_is_instance_object_user(self):
        """ Test id created """
        obj = Review()
        self.assertTrue(type(obj) is Review)

    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = Review()
        self.assertTrue(type(obj.id) == str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different
        with two instance object """
        obj = Review()
        obj2 = Review()
        self.assertTrue(obj.id != obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Review()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Review()
        obj2 = Review()
        d1 = obj.created_at
        d2 = obj2.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = Review()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = Review()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute
        has been well created with multiple instance"""
        obj = Review()
        obj2 = Review()
        d1 = obj.updated_at
        d2 = obj2.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = Review()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_is_place_id_updated(self):
        """ Test that place_id attribute is well updated"""
        obj = Review()
        obj.place_id = "Thibaut"
        self.assertTrue(obj.place_id == "Thibaut")

    def test_is_user_id_updated(self):
        """ Test that user_id attribute is well updated"""
        obj = Review()
        obj.user_id = "Thibaut"
        self.assertTrue(obj.user_id == "Thibaut")

    def test_is_text_updated(self):
        """ Test that text attribute is well updated"""
        obj = Review()
        obj.text = "Thibaut"
        self.assertTrue(obj.text == "Thibaut")

    """
        kwargs
    """
    """
    def test_is_kwargs_instance(self):
        obj = Review()
        save_dict = obj.to_dict()
        new_obj = Review(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())
    """
    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is
        instance created_at to date object """
        obj = Review()
        save_dict = obj.to_dict()
        new_obj = Review(**save_dict)
        self.assertTrue(type(new_obj.created_at) is datetime)
    """
    def test_is_kwargs_ignore_one_attribute(self):
        obj = BaseModel()
        save_dict = obj.to_dict()
        new_obj = BaseModel(**save_dict)
        with self.assertRaises(AttributeError):
            new_obj.__class__
    """
    """
    Method to_dict()
    """
    def test_is_to_dict_return_a_dict(self):
        """ Test that the to_dict()
        method return well a dictionnary """
        obj = Review()
        s = obj.to_dict()
        self.assertTrue(type(s) is dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = Review()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertTrue(type(s[i]) is str)

    """
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = Review()
        s = str(obj)
        self.assertTrue(type(s) is str)

    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = Review()
        s = str(obj)
        self.assertTrue("Review" in s)
