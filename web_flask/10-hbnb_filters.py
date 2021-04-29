#!/usr/bin/python3
"""
    routes
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
