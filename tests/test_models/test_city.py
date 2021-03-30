#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
import os.path
from os import path
from MySQLdb import _mysql
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import MySQLdb


class TestCity(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_type_name(self):
        """ Test that type name is str"""
        obj = City()
        obj.name = "dzdz"
        n = getattr(obj, "name")
        self.assertIsInstance(n, str)

    # @unittest.skipIf(
    #      "HBNB_TYPE_STORAGE" not in os.environ or
    #      os.environ['HBNB_TYPE_STORAGE'] == "fs", "fs engine")
    # def test_create_c_in_database(self):
    #    """ Test """
    #    a = "localhost"
    #    b = "hbnb_test"
    #    c = "hbnb_test_pwd"
    #    d = "hbnb_test_db"
    #    with patch('sys.stdout', new=StringIO()) as f:
    #        HBNBCommand().onecmd('create State name="calif"')
    #    db = MySQLdb.connect(host=a, user=b, passwd=c, db=d, port=3306)
    #    x = db.cursor()
    #    x.execute("""SELECT * FROM states""")
    #    i = x.fetchall()[0][0]
    #    db = MySQLdb.connect(host=a, user=b, passwd=c, db=d, port=3306)
    #    x = db.cursor()
    #    x.execute("""SELECT COUNT(id) FROM cities""")
    #    nb_cities_before = x.fetchall()[0][0]
    #    with patch('sys.stdout', new=StringIO()) as f:
    #        s = 'create City state_id="{}" name="S"'
    #        HBNBCommand().onecmd(s.format(i))
    #    db = MySQLdb.connect(host=a, user=b, passwd=c, db=d, port=3306)
    #    x = db.cursor()
    #    x.execute("""SELECT COUNT(id) FROM cities""")
    #    nb_cities_after = x.fetchall()[0][0]
    #    self.assertNotEqual(nb_cities_before, nb_cities_after)

    def test_type_state_id(self):
        """ Test that type state_id is str"""
        obj = City()
        obj.state_id = "dzdz"
        n = getattr(obj, "state_id")
        self.assertIsInstance(n, str)

    """Basic instanciation object__init__"""
    def test_user_id_created(self):
        """ Test id created """
        obj = City()
        self.assertTrue(obj.id is not None)
        self.assertTrue(type(obj) is City)

    def test_user_is_instance_object_user(self):
        """ Test id created """
        obj = City()
        self.assertTrue(type(obj) is City)

    def test_is_id_is_string(self):
        """ Test id is a string"""
        obj = City()
        self.assertTrue(type(obj.id) == str)

    def test_is_id_different_multiple_instance(self):
        """ Test that id is different
        with two instance object """
        obj = City()
        obj2 = City()
        self.assertTrue(obj.id != obj2.id)

    def test_is__created_date_is_created(self):
        """ Test that a date has been well created """
        obj = City()
        self.assertTrue(obj.created_at is not None)

    def test_is_created_date_is_created(self):
        """ Test that a date has been well created """
        obj = City()
        obj2 = City()
        d1 = obj.created_at
        d2 = obj2.created_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is__created_date_is_object_datatime(self):
        """ Test that created_at is a object date"""
        obj = City()
        self.assertTrue(type(obj.created_at) == datetime)

    def test_is_updated_at_is_created(self):
        """ Test that updated_at attribute has been well created """
        obj = City()
        self.assertTrue(obj.updated_at is not None)

    def test_is_updated_at_is_created_multiple_instance(self):
        """ Test that updated_at attribute
        has been well created with multiple instance"""
        obj = City()
        obj2 = City()
        d1 = obj.updated_at
        d2 = obj2.updated_at
        self.assertTrue(d1 is not None and d2 is not None)

    def test_is_updated_at_is_object_datatime(self):
        """ Test that updated_at is a object date"""
        obj = City()
        self.assertTrue(type(obj.updated_at) == datetime)

    def test_is_state_id_updated(self):
        """ Test that state_id attribute is well updated"""
        obj = City()
        obj.state_id = "Thibaut"
        self.assertTrue(obj.state_id == "Thibaut")

    def test_is_name_updated(self):
        """ Test that name attribute is well updated"""
        obj = City()
        obj.name = "Thibaut"
        self.assertTrue(obj.name == "Thibaut")

    """
        kwargs
    """
    """
    def test_is_kwargs_instance(self):
        obj = City()
        save_dict = obj.to_dict()
        new_obj = City(**save_dict)
        self.assertTrue(save_dict == new_obj.to_dict())
    """
    def test_is_kwargs_created_at_date_object(self):
        """ Test that kwargs is instance created_at to date object """
        obj = City()
        save_dict = obj.to_dict()
        new_obj = City(**save_dict)
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
        obj = City()
        s = obj.to_dict()
        self.assertTrue(type(s) is dict)

    def test_is_to_dict_updated_at_is_str(self):
        """ Test that to_dict() updated_at is str in dictionary"""
        obj = City()
        s = obj.to_dict()
        for i in s:
            if i == "updated_at":
                self.assertTrue(type(s[i]) is str)

    """
        Method __str__
    """
    def test_is_str_return_a_string(self):
        """ Test that __str__return well a string """
        obj = City()
        s = str(obj)
        self.assertTrue(type(s) is str)

    def test_is_str_return_the_correct_class_name(self):
        """ Test that __str__ user as class name """
        obj = City()
        s = str(obj)
        self.assertTrue("City" in s)
