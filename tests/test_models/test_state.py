#!/usr/bin/python3
""" """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
import os.path
from os import path
from MySQLdb import _mysql
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestState(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    # @unittest.skipIf(
    #      "HBNB_TYPE_STORAGE" not in os.environ or
    #      os.environ['HBNB_TYPE_STORAGE'] == "fs", "fs engine")
    # def test_create_state_in_database(self):
    #    """ Test """
    #    a = "localhost"
    #    b = "hbnb_test"
    #    c = "hbnb_test_pwd"
    #    d = "hbnb_test_db"
    #    db = _mysql.connect(host=a, user=b, passwd=c, db=d)
    #    db.query("""SELECT COUNT(id) FROM states""")
    #    r = db.store_result().fetch_row(how=1, maxrows=0)
    #    with patch('sys.stdout', new=StringIO()) as f:
    #        HBNBCommand().onecmd('create State name="t"')
    #    db.query("""SELECT COUNT(id) FROM states""")
    #    t = db.store_result().fetch_row(how=1, maxrows=0)
    #    self.assertNotEqual(t[0]['COUNT(id)'], r[0]['COUNT(id)'])

    def test_type_name(self):
        """ Test that type name is str"""
        obj = State()
        obj.name = "dzdz"
        n = getattr(obj, "name")
        self.assertIsInstance(n, str)

    """Basic instanciation object__init__"""
    def test_user_id_created(self):
        """ Test id created """
        obj = State()
        self.assertTrue(obj.id is not None)
        self.assertTrue(type(obj) is State)

    def test_user_is_instance_object_user(self):
        """ Test id created """
        obj = State()
        self.assertTrue(type(obj) is State)

    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = State()
        self.assertTrue(type(obj.id) == str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different
        with two instance object """
        obj = State()
        obj2 = State()
        self.assertTrue(obj.id != obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = State()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = State()
        obj2 = State()
        d1 = obj.created_at
        d2 = obj2.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = State()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = State()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at
        attribute has been well created with multiple instance"""
        obj = State()
        obj2 = State()
        d1 = obj.updated_at
        d2 = obj2.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = State()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_is_name_updated(self):
        """ Test that name attribute is well updated"""
        obj = State()
        obj.name = "Thibaut"
        self.assertTrue(obj.name == "Thibaut")

    """
        kwargs
    """
    """
    def test_is_kwargs_instance(self):
        obj = State()
        save_dict = obj.to_dict()
        new_obj = State(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())
    """
    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is
        instance created_at to date object """
        obj = State()
        save_dict = obj.to_dict()
        new_obj = State(**save_dict)
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
        obj = State()
        s = obj.to_dict()
        self.assertTrue(type(s) is dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = State()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertTrue(type(s[i]) is str)
    """
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = State()
        s = str(obj)
        self.assertTrue(type(s) is str)

    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = State()
        s = str(obj)
        self.assertTrue("State" in s)
