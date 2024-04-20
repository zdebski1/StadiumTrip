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




# @app.route("/visits", methods=['POST'])
# def addNewVisit():
#     """
#     This endpoint adds a new visit.
#     ---
#     parameters:
#       - name: visitStadium
#         in: formData
#         type: string
#         required: true
#         description: The name of the stadium visited.
#       - name: visitDate
#         in: formData
#         type: string
#         format: date
#         required: false
#         description: The date of the visit.
#       - name: visitPeople
#         in: formData
#         type: string
#         required: false
#         description: The list of people in your group.
#     responses:
#       200:
#         description: Visit added successfully.
#         content:
#           application/json:
#             schema:
#               type: object
#               properties:
#                 message:
#                   type: string
#                   description: Success message.
#     """
#     # try:
#     requestData = request.form
    
#     visitStadium = requestData.get('visitStadium')
#     visitDate = requestData.get('visitDate')
#     visitPeople = requestData.get('visitPeople')

#     visitDate_date = dt.datetime.strptime(visitDate, '%Y-%m-%d').date()

#     vistInstance = Visit(visitStadium, visitDate_date, visitPeople)

#     vistInstance.saveVisit()

#     return jsonify({'message': 'Visit added successfully'})
#     # except Exception as e:
#     #     print(e)


# if __name__ == "__main__":
#     app.run(debug=True)