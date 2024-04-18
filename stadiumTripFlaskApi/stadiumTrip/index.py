from flask import Flask, jsonify, request
from flasgger import Swagger

from model.Visit import Visit
from config.Common import Utils

app = Flask(__name__)
swagger = Swagger(app)



UtilsInstance = Utils()

visitsCSV: str = 'C:/Projects/Repos/StadiumTrip/stadiumTripFlaskApi/stadiumTrip/data/visits.csv'
returnVisits = UtilsInstance.returnCsvToList(visitsCSV)

@app.route("/visits")
def returnStadiumsVisited():
    return jsonify(returnVisits)