from flask import Flask, jsonify, request
from flasgger import Swagger

from model.Visit import Visit


app = Flask(__name__)
swagger = Swagger(app)

# Initialize an empty list to store visits
visits = ['{"StadiumName" : "Fenway Park"}']

@app.route("/visits")
def hello_world():
    return jsonify(visits)