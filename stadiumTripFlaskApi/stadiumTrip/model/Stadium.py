import pandas as pd
from config.Common import Utils

class Stadium(object):

    @staticmethod 
    def returnStadiumName():
        
        UtilsInstance = Utils()

        stadiumName = UtilsInstance.returnSqlDataToPandasDf('dbo','vw_ListOfStadiums')

        stadiumList = stadiumName['stadiumname'].tolist()

        return stadiumList