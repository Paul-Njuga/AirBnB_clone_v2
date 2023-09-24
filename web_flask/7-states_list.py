#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states(states=None):
    '''Displays a HTML page that lists states'''
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session():
    '''Removes the current SQLAlchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
