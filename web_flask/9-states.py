#!/usr/bin/python3
"""
    routes for the project
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


@app.route('/states', strict_slashes=False)
def get_all_states_route():
    """ get all states and give to the template"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def get_states_by_id_route(id):
    """ get all states by id and give to the template"""
    states = storage.all(State)
    for k, v in states.items():
        if v.id == id:
            return render_template('9-states.html', state=v)
    return render_template('9-states.html', state=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
