import datetime as dt

from  .Stadium import Stadium

class Visit(object):
    def __init__(self, visitStadium: str, visitDate = dt.datetime, visitPeople = list): 
        stadiums = Stadium.returnStadiumName()
        if visitStadium not in stadiums:
            raise ValueError(f"Invalid stadium, Please use a stadium in this list: {stadiums}")
        
        self.visitStadium = visitStadium
        self.visitDate = visitDate
        self.visitPeople = visitPeople


    def __repr__(self) -> str:
         people_str = ', '.join(self.visitPeople).strip("[]'")
         
         return 'Visited: {self.visitStadium} on {self.visitDate} with {people_str}'.format(self=self,people_str=people_str)