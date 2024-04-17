from flask import Flask, jsonify, request
from flasgger import Swagger

from model.Visit import Visit


app = Flask(__name__)
swagger = Swagger(app)

# Initialize an empty list to store visits
visits = []

@app.route('/visits', methods=['POST'])
def add_visit():
    """
    Add a new visit
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Visit
          required:
            - visitStadium
          properties:
            visitStadium:
              type: string
              description: The name of the stadium
            visitDate:
              type: string
              description: The date of the visit
            visitPeople:
              type: array
              description: List of people visiting the stadium
              items:
                type: string
    responses:
      201:
        description: Visit added successfully
      400:
        description: Bad request
    """
    data = request.get_json()  # Get the JSON data from the request body
    
    try:
        # Extract required fields from the JSON data
        visitStadium = data['visitStadium']
        visitDate = data.get('visitDate')  # Optional, default to None if not provided
        visitPeople = data.get('visitPeople', [])  # Optional, default to an empty list if not provided

        # Create a new Visit object
        new_visit = Visit(visitStadium, visitDate, visitPeople)
        
        # Append the new visit to the visits list
        visits.append(new_visit)

        return jsonify({'message': 'Visit added successfully'}), 201  # Return a success response
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error response if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)