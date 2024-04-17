#!/bin/sh
export FLASK_APP=./stadiumTrip/index.py
export PYTHONPATH=./stadiumTrip
pipenv run flask --debug run -h 0.0.0.0
