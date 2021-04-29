#!/usr/bin/python3
"""
    setup 5 routes and start the app
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """simple route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ /c route """
    tmp = text.replace('_', ' ')
    return 'C {}'.format(tmp)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ /python and optional param """
    tmp = text.replace('_', ' ')
    return 'Python {}'.format(tmp)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ /number route """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ /number_template route """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
