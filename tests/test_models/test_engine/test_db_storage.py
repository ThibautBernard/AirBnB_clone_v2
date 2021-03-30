#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.city import City
from models.state import State
from models import storage
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    @unittest.skipIf(type(storage) == FileStorage, "haha")
    def test_all_method(self):
        d = storage.all()
        self.assertTrue(type(d) == dict)
