import csv
import os
import psycopg2

from config.Secrets import Secrets


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
   

   
   
   def returnSqlData(self, schema, tableName):
        SecretsInstance = Secrets()
        
        try:
            conn = psycopg2.connect(
                database=f"{SecretsInstance.postGreSqlDatabase}",
                user=f"{SecretsInstance.postGreSqlUser}",
                password=f"{SecretsInstance.postGreSqlPassword}",
                host=f"{SecretsInstance.postGreSqlHost}",
                port=f"{SecretsInstance.postGreSqlPort}"
            )
            
            conn.autocommit = True
            cursor = conn.cursor()
            query = f'''SELECT * FROM {schema}.{tableName}'''
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            
            return result
        
        except Exception as e:
            print(e)