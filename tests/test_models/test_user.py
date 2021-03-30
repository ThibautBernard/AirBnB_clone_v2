#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import os.path
from os import path
from MySQLdb import _mysql
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestUser(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    """Basic instanciation object__init__"""
    def test_user_id_created(self):
        """ Test id created """
        obj = User()
        self.assertTrue(obj.id is not None)
        self.assertEqual(type(obj), User)

    def test_type_attr(self):
        """ Test attr type"""
        obj = User()
        obj.email = "dzdz"
        obj.password = "dzdzd"
        obj.first_name = "dzdz"
        obj.last_name = "édddz"
        self.assertEqual(type(obj.email), str)
        self.assertEqual(type(obj.password), str)
        self.assertEqual(type(obj.first_name), str)
        self.assertEqual(type(obj.last_name), str)

    def test_user_inherit_baseModel(self):
        """ Test that user is subclass to basemode"""
        obj = User()
        self.assertIsInstance(obj, BaseModel)

    def test_type_email(self):
        """ Test that type email is str"""
        obj = User()
        obj.email = "dzdzdz"
        n = getattr(obj, "email")
        self.assertIsInstance(n, str)

    def test_type_pwd(self):
        """ Test that type pswd is str"""
        obj = User()
        obj.password = "ss"
        n = getattr(obj, "password")
        self.assertIsInstance(n, str)

    def test_type_first_name(self):
        """ Test that type first_name is str"""
        obj = User()
        obj.first_name = "Kjdz"
        n = getattr(obj, "first_name")
        self.assertIsInstance(n, str)

    def test_type_last_name(self):
        """ Test that type last_name is str"""
        obj = User()
        obj.last_name = "Thibaut"
        n = getattr(obj, "last_name")
        self.assertIsInstance(n, str)

    def test_user_inherit_basemodel(self):
        """ Test that user inherit from BaseModel """
        obj = User()
        self.assertIsInstance(obj, BaseModel)

    def test_user_is_instance_object_user(self):
        """ Test id created """
        obj = User()
        self.assertEqual(type(obj), User)

    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = User()
        self.assertEqual(type(obj.id), str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different with two instance object """
        obj = User()
        obj2 = User()
        self.assertNotEqual(obj.id, obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = User()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = User()
        obj2 = User()
        d1 = obj.created_at
        d2 = obj2.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = User()
        self.assertEqual(type(obj.created_at), datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = User()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute
        has been well created with multiple instance"""
        obj = User()
        obj2 = User()
        d1 = obj.updated_at
        d2 = obj2.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = User()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_is_email_updated(self):
        """ Test that email attribute is well updated"""
        obj = User()
        obj.email = "Thibaut"
        self.assertEqual(obj.email, "Thibaut")

    def test_is_password_updated(self):
        """ Test that password attribute is well updated"""
        obj = User()
        obj.password = "Thibaut"
        self.assertEqual(obj.password, "Thibaut")

    def test_is_first_name_updated(self):
        """ Test that first_name attribute is well updated"""
        obj = User()
        obj.first_name = "Thibaut"
        self.assertEqual(obj.first_name, "Thibaut")

    def test_is_last_name_updated(self):
        """ Test that last_name attribute is well updated"""
        obj = User()
        obj.last_name = "Thibaut"
        self.assertEqual(obj.last_name, "Thibaut")

    """
        kwargs
    """
    """def test_is_kwargs_instance(self):
        obj = User()
        save_dict = obj.to_dict()
        new_obj = User(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())
    """
    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is instance created_at to date object """
        obj = User()
        save_dict = obj.to_dict()
        new_obj = User(**save_dict)
        self.assertEqual(type(new_obj.created_at), datetime)
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
        """ Test that the to_dict() method return well a dictionnary """
        obj = User()
        s = obj.to_dict()
        self.assertEqual(type(s), dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = User()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertEqual(type(s[i]), str)
    """
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = User()
        s = str(obj)
        self.assertEqual(type(s), str)

    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = User()
        s = str(obj)
        self.assertTrue("User" in s)

    """
        Method save()
    def test_is_save_update_well(self):
        x = BaseModel()
        x.save()
        self.assertTrue(x.created_at != x.updated_at)
    def test_is_save_update(self):
        s = BaseModel()
        h = s.updated_at
        s.save()
        self.assertTrue(h != s.updated_at)
    """
