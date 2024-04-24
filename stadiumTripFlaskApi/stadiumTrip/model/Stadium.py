import json

from config.Common import Utils

class Stadium(object):

    @staticmethod 
    def returnStadiumName():
        
        UtilsInstance = Utils()

        stadiumName = UtilsInstance.returnSqlData('dbo','vw_ListOfStadiums')

        stadiumList = [row[0] for row in stadiumName]


        return stadiumList