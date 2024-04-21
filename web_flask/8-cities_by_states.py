#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def city_state_list():
    """
        method to render states from storage
    """
    states = storage.all('State').values()
    return render_template("8-cities_by_states.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
