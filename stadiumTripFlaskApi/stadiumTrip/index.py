from flask import Flask, jsonify, request
from stadiumTrip.model.Visit import Visit


app = Flask(__name__)

visits = [
    { 'stadium': 'FenwayPark', 'visit': 'yes' }
]


@app.route('/visits')
def get_visits():
    return jsonify(visits)


@app.route('/visits', methods=['POST'])
def add_visits():
    visits.append(request.get_json())
    return '', 204