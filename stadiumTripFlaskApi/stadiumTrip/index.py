from flask import Flask, jsonify, request
from flasgger import Swagger
import datetime as dt

from model.Visit import Visit
from config.Common import Utils

app = Flask(__name__)
swagger = Swagger(app)



UtilsInstance = Utils()

visitsCSV: str = 'C:/Projects/Repos/StadiumTrip/stadiumTripFlaskApi/stadiumTrip/data/visits.csv'

@app.route("/visits", methods=['GET'])
def returnStadiumsVisited():
    
    """
    This endpoint returns a list of stadiums visited.
    ---
    responses:
      200:
        description: A list of stadiums visited.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return jsonify(UtilsInstance.returnCsvToList(visitsCSV))




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