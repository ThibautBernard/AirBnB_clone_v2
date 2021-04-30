#!/usr/bin/python3
"""
    routes
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import os
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def get_all_states_route():
    """ get all states and give to the template"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_route():
    """ get all cities by states and give to the template"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
