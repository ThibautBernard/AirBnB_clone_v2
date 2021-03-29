#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            nullable=False
        ),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'),
            nullable=False
        )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"))
    user_id = Column(String(60), ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            # back_populates="place_amenities",
            viewonly=False
        )
    amenity_ids = []

    @property
    def reviews(self):
        revs = []
        for k, rev in storage.all(Review).items():
            if rev.place_id == self.id:
                revs.append(rev)
        return revs

    @property
    def amenities(self):
        amens = []
        for k, amen in storage.all(Amenity).items():
            if amen.place_id == self.id:
                amens.append(amen)
        return amens

    @amenities.setter
    def amenities(self, amen):
        if isinstance(amen, Amenity):
            Place.amenity_ids.append(amen.id)
