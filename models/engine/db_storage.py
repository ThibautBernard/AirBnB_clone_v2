#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
import MySQLdb
import os
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()


class DBStorage:
    """This class manages storage of hbnb models in Database"""
    __engine = None
    __session = None
    classes = [City, State]
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                           os.environ['HBNB_MYSQL_USER'], os.environ['HBNB_MYSQL_PWD'],
                           os.environ['HBNB_MYSQL_HOST'], os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
#        if os.environ["HBNB_ENV"] == "test":
#            Base.metadata.delete_all(self.__engine)

    def list_to_dict(self, l):
        d = {}
        for obj in l:
            key = obj.__class__.__name__ + '.' + obj.id
            d[key] = obj
        return d
    
    def all(self, cls=None):
        d = {}
        if cls == None:
            tmp_l = []
            for c in self.classes:
                for o in self.__session.query(c).all():
                    tmp_l.append(o)
            return self.list_to_dict(tmp_l)
        else:
            l = self.__session.query(cls).all()
            return self.list_to_dict(l) 

    def new(self, obj):
        if obj:
            self.__session.add(obj)
            self.save()   
    
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.query(obj).delete()
    
    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit="false")
        self.__session = Session()
        