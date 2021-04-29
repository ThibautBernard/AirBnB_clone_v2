#!/usr/bin/python3
"""
    setup 3 routes and start the app
"""
from flask import Flask
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
def arg1(text):
    tmp = text.replace('_', ' ')
    return 'C {}'.format(tmp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
