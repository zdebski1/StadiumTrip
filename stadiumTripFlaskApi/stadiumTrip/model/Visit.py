import datetime as dt
import json

from .Stadium import Stadium
from config.Common import Utils


class Visit(object):
    def __init__(self, visitStadium: str, visitDate = dt.datetime, visitPeople = list): 
        stadiums = Stadium.returnStadiumName()
        if visitStadium not in stadiums:
            raise ValueError(f"{self.visitStadium} is an invalid stadium, Please use a stadium in this list: {stadiums}")
        
        self.visitStadium = visitStadium
        self.visitDate = visitDate
        self.visitPeople = visitPeople

       
    def saveVisit (self):

        utilsInstance = Utils()

        isDeleted: int  = 0
        columnName: list = ["visitStadium", "visitDate", "visitPeople","isDeleted"]
        data: list = [self.visitStadium, self.visitDate, self.visitPeople,isDeleted]
      
        utilsInstance.saveDataToSql(columnName,'dbo','visits',data)

        print(f'Saved Visit {self.visitStadium} on {self.visitDate} with {self.visitPeople}')