import json

from config.Common import Utils

class Stadium(object):

    @staticmethod 
    def returnStadiumName():
        
        UtilsInstance = Utils()

        stadiumName = UtilsInstance.returnSqlData('dbo','vw_ListOfStadiums')

        stadiumList = [row[0] for row in stadiumName]


        return stadiumList
    

    @staticmethod 
    def returnAllStadiumData():
        f = open('C:/Projects/Repos/StadiumTrip/stadiumTripFlaskApi/stadiumTrip/data/Stadium.json')
        data = json.load(f)

        stadiumInfo = []

        for i in data['Stadiums']:
            stadiumInfo.append(i)

        f.close()
            
        return stadiumInfo