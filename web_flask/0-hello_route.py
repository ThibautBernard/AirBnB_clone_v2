#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
#SERVER_NAME='0.0.0.0'

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
app.run(host='0.0.0.0', port=5000)
