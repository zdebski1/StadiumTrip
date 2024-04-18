from flask import Flask, jsonify, request
from flasgger import Swagger
import datetime as dt

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





@app.route("/visits", methods=['POST'])
def addNewVisit():

    requestData = request.json


    visitStadium = requestData.get('visitStadium')
    visitDate = requestData.get('visitDate')
    visitPeople = requestData.get('visitPeople')

    visitDate_date = dt.datetime.strptime(visitDate, '%Y-%m-%d').date()
    
    vistInstance = Visit(visitStadium, visitDate_date, visitPeople)
    
    vistInstance.saveVisit()
    
    return jsonify({'message': 'Visit added successfully'})


if __name__ == "__main__":
    app.run(debug=True)