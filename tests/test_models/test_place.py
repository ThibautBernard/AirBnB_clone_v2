#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
import os.path
from os import path
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import MySQLdb


class TestPlace(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type_city_id(self):
        """ Test type"""
        obj = Place()
        obj.city_id = "dzdz"
        n = getattr(obj, "city_id")
        self.assertIsInstance(n, str)

    def test_type_user_id(self):
        """ Test type"""
        obj = Place()
        obj.user_id = "dzdz"
        n = getattr(obj, "user_id")
        self.assertIsInstance(n, str)

    def test_type_description(self):
        """ Test type"""
        obj = Place()
        obj.description = "zdzdz"
        n = getattr(obj, "description")
        self.assertIsInstance(n, str)

    def test_type_number_rooms(self):
        """ Test type"""
        obj = Place()
        obj.number_rooms = 2
        n = getattr(obj, "number_rooms")
        self.assertIsInstance(n, int)

    def test_type_number_bath(self):
        """ Test type"""
        obj = Place()
        obj.number_bathrooms = 5
        n = getattr(obj, "number_bathrooms")
        self.assertIsInstance(n, int)

    def test_type_max_guet(self):
        """ Test type"""
        obj = Place()
        obj.max_guest = 12
        n = getattr(obj, "max_guest")
        self.assertIsInstance(n, int)

    def test_type_price_by_night(self):
        """ Test type"""
        obj = Place()
        obj.price_by_night = 6
        n = getattr(obj, "price_by_night")
        self.assertIsInstance(n, int)

    def test_type_latitude(self):
        """ Test type"""
        obj = Place()
        obj.latitude = 5.5
        n = getattr(obj, "latitude")
        self.assertIsInstance(n, float)

    def test_type_long(self):
        """ Test type"""
        obj = Place()
        obj.longitude = 6.6
        n = getattr(obj, "longitude")
        self.assertIsInstance(n, float)

    def test_type_ameni_id(self):
        """ Test type"""
        obj = Place()
        obj.amenity_id = []
        n = getattr(obj, "amenity_ids")
        self.assertIsInstance(n, list)

    def test_type_name(self):
        """ Test that type name is str"""
        obj = Place()
        obj.name = "ddzdz"
        n = getattr(obj, "name")
        self.assertIsInstance(n, str)

    """Basic instanciation object__init__"""
    def test_Place_id_created(self):
        """ Test id created """
        obj = Place()
        self.assertTrue(obj.id is not None)
        self.assertTrue(type(obj) is Place)

    def test_Place_is_instance_object_user(self):
        """ Test id created """
        obj = Place()
        self.assertTrue(type(obj) is Place)

    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = Place()
        self.assertTrue(type(obj.id) == str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different with two instance object """
        obj = Place()
        obj2 = Place()
        self.assertTrue(obj.id != obj2.id)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Place()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = Place()
        obj2 = Place()
        d1 = obj.created_at
        d2 = obj2.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = Place()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = Place()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute
        has been well created with multiple instance"""
        obj = Place()
        obj2 = Place()
        d1 = obj.updated_at
        d2 = obj2.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = Place()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_is_city_id_updated(self):
        """ Test that city_id attribute is well updated"""
        obj = Place()
        obj.city_id = "Thibaut"
        self.assertTrue(obj.city_id == "Thibaut")

    def test_is_name_updated(self):
        """ Test that name attribute is well updated"""
        obj = Place()
        obj.name = "Thibaut"
        self.assertTrue(obj.name == "Thibaut")

    def test_is_user_id_updated(self):
        """ Test that user_id attribute is well updated"""
        obj = Place()
        obj.user_id = "Thibaut"
        self.assertTrue(obj.user_id == "Thibaut")

    def test_is_latitude_updated(self):
        """ Test that latitude attribute is well updated"""
        obj = Place()
        obj.latitude = 5.4
        self.assertTrue(obj.latitude == 5.4)

    """
        kwargs
    """
    """
    def test_is_kwargs_instance(self):
        obj = Place()
        save_dict = obj.to_dict()
        new_obj = Place(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())
    """
    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is instance created_at to date object """
        obj = Place()
        save_dict = obj.to_dict()
        new_obj = Place(**save_dict)
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
        """ Test that the to_dict() method return well a dictionnary """
        obj = Place()
        s = obj.to_dict()
        self.assertTrue(type(s) is dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = Place()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertTrue(type(s[i]) is str)

    """
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = Place()
        s = str(obj)
        self.assertTrue(type(s) is str)

    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = Place()
        s = str(obj)
        self.assertTrue("Place" in s)
