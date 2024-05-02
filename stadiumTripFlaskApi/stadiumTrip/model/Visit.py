import datetime as dt
import json
import pandas as pd
import itertools

from .Stadium import Stadium
from config.Common import Utils


class Visit(object):

    utilsInstance = Utils()
    isDeleted = 0
    visitDfStruct = ['visitStadium', 'visitDate', 'visitPeople', 'isDeleted']
    saveToSqlStruct = ['stadiumid', 'visitDate', 'visitPeople', 'isDeleted']

    def __init__(self, visitStadium: str, visitDate = dt.datetime, visitPeople = list): 
        stadiums = Stadium.returnStadiumName()
        if visitStadium not in stadiums:
            raise ValueError(f"{self.visitStadium} is an invalid stadium, Please use a stadium in this list: {stadiums}")
        
        self.visitStadium = visitStadium
        self.visitDate = visitDate
        self.visitPeople = visitPeople

       
    def saveVisit (self):

        columnName: list = self.saveToSqlStruct
        data = self._createVisitToSave()
        flattened_data = list(itertools.chain.from_iterable(data))
      
        self.utilsInstance.saveDataToSql(columnName,'dbo','visits',flattened_data)

        print(f'Saved Visit {self.visitStadium} on {self.visitDate} with {self.visitPeople}')


    def _returnStadiumID(self):
        schema = 'tlkp'
        table = 'stadium'
        
        stadium = self.utilsInstance.returnSqlDataToPandasDf(schema, table)
        filtered_stadium = stadium[stadium['stadiumname'] == self.visitStadium]
        return filtered_stadium

    def _createVisitToSave(self):
        
        input = [self.visitStadium, self.visitDate, self.visitPeople, self.isDeleted]

        visitDf = pd.DataFrame([input], columns=self.visitDfStruct)
        
        stadiumIdDf = self._returnStadiumID()
        stadiumIdDf.rename(columns={'stadiumname': 'visitStadium'}, inplace=True)

        visitJoinedDf = pd.merge(stadiumIdDf[['stadiumid','visitStadium']], 
                                 visitDf[self.visitDfStruct],
                                 on='visitStadium', how='inner')
        
        finalVisitDf = visitJoinedDf[self.saveToSqlStruct]
        finalVisitList = finalVisitDf.values.tolist()


        return finalVisitList