import csv
import os
import psycopg2

from config.Secrets import Secrets


class Utils (object):
     def returnSqlData(self, schema:str, tableName:str):
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


     def saveDataToSql(self, intoColumns: list, intoSchema: str, intoTableName: str, fromValues: list):
        SecretsInstance = Secrets()
    
        try:
            conn = psycopg2.connect(
                database=SecretsInstance.postGreSqlDatabase,
                user=SecretsInstance.postGreSqlUser,
                password=SecretsInstance.postGreSqlPassword,
                host=SecretsInstance.postGreSqlHost,
                port=SecretsInstance.postGreSqlPort
            )
            
            conn.autocommit = True
            cursor = conn.cursor()
            placeholders = ','.join(['%s'] * len(intoColumns))
            query = f'INSERT INTO {intoSchema}.{intoTableName} ({", ".join(intoColumns)}) VALUES ({placeholders});'
            cursor.execute(query, fromValues)  
            conn.close()
        
        except Exception as e:
            print(e)

     def returnVisits(self):

        utilsInstance = Utils()

        previousVisits = utilsInstance.returnSqlData("dbo","vw_stadiumsVisited") 
        return previousVisits           
