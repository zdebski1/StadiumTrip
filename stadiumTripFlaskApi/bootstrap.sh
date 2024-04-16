#!/bin/sh
export FLASK_APP=./stadiumTrip/index.py
pipenv run flask --debug run -h 0.0.0.0

app.run()