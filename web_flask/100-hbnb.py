#!/usr/bin/python3
"""
    routes hbnb_clone
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
import os
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """after each request"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters_route():
    """ get all states and amenities objets
        and give to the template to fill the popover
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def home_page_route():
    """
        give to the template all objects
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    
    return render_template(
            '100-hbnb.html',
            states=states,
            amenities=amenities,
            places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
