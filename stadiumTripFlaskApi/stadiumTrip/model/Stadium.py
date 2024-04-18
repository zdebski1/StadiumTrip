import json


class Stadium(object):

    @staticmethod 
    def returnStadiumName():
        f = open('C:/Projects/Repos/StadiumTrip/stadiumTripFlaskApi/stadiumTrip/data/Stadium.json')
        data = json.load(f)

        stadiumName = []

        for i in data['Stadiums']:
            stadiumName.append(i['stadiumName'])

        f.close()
        
        return stadiumName
    

    @staticmethod 
    def returnAllStadiumData():
        f = open('C:/Projects/Repos/StadiumTrip/stadiumTripFlaskApi/stadiumTrip/data/Stadium.json')
        data = json.load(f)

        stadiumInfo = []

        for i in data['Stadiums']:
            stadiumInfo.append(i)

        f.close()
            
        return stadiumInfo