import csv
import os 

class Utils (object):
   
   def saveDataToCSV(self, fileName: str, header: list , dataColumns: list):
        file_exists = os.path.isfile(fileName)


        with open(fileName, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            if not file_exists:
                csv_writer.writerow(header)
                
            csv_writer.writerow(dataColumns)


   def readDataFromCsv(self, fileName: str):
        file_exists = os.path.isfile(fileName)

        data = []

        if not file_exists:
            print('File does not exist, please check filename and try again.')
        else:            
            with open(fileName, 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    data.append(row)
                    
        return data
   
   
   def returnCsvToList (self, fileName: str):
        
        visits = self.readDataFromCsv(fileName)
        return visits