#!/usr/bin/python3
"""
    routes for the project
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_all_states_route():
    """ get all states and give to the template"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """after each request"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
