#!/usr/bin/python3
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
import os.path
from models import storage
from os import path
"""
    UnitTest for the command line interpreter
"""


class TestConsole(unittest.TestCase):

    def setUp(self):
        FileStorage._FileStorage__objects = {}
    # if os.path.exists("file.json"):
    # os.remove("file.json")
    # def tearDown(self):
    #    if os.path.exists("file.json"):
    #        os.remove("file.json")

    def test_create_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    def test_show(self):
        """Test show command."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    """
        Create cmd
    """
    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="Sa" state_id="0001"')
        self.assertTrue(os.path.exists("file.json"))

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_one_false_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="Sa" statedz="0001"')
        f = FileStorage()
        f.reload()
        with self.assertRaises(AttributeError) as cm:
            for k, v in f._FileStorage__objects.items():
                v.foo
        tmp = cm.exception
        self.assertEqual("'City' object has no attribute 'foo'", str(tmp))

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_one_good_arguments_with_space_in_name(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="Sa" state_id="0001"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "Sa")

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_good_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="Paris" state_id="0001"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "Paris")
            self.assertEqual(v.state_id, "0001")

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_boolean_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="M" longitude=-122.431297')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.longitude, -122.431297)

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_name_And_underscore_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="My_little_house"')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.name, "My little house")

    @unittest.skipIf(
        "HBNB_TYPE_STORAGE" in os.environ and
        os.environ['HBNB_TYPE_STORAGE'] == "db", "db engine")
    def test_create_with_integer_value_arguments(self):
        """ Test that create an object with args """
        # self.assertFalse(os.path.exists("file.json"))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place name="M" price_by_night=300')
        f = FileStorage()
        f.reload()
        for k, v in f._FileStorage__objects.items():
            self.assertEqual(v.price_by_night, 300)
