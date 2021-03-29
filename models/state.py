#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from sqlalchemy.ext.declarative import declarative_base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",  cascade="all, delete")

    @property
    def cities(self):
        l = []
        for k, v in storage.all(City).items():
            if v.state_id == self.id:
                l.append(v)
        return l
