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
    pass
