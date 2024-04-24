from config.DatabasePool import DatabasePool

class Utils (object):
    def __init__(self):
        self.db = DatabasePool()

    def returnSqlData(self, schema:str, tableName:str):
   
        try:
            conn = self.db.getConnection()

            if (conn):
                print("Successfully recived connection from connection pool")
                cursor = conn.cursor()

                query = f'''SELECT * FROM {schema}.{tableName}'''
                cursor.execute(query)
                result = cursor.fetchall()

                cursor.close()
                self.db.releaseConnection(conn)
                print("Put away a PostgreSQL connection")
            
            return result
        
        except Exception as e:
            print(e)


    def saveDataToSql(self, intoColumns: list, intoSchema: str, intoTableName: str, fromValues: list):
         
        try:
            conn = self.db.getConnection()

            if (conn):
                print("Successfully recived connection from connection pool")
                cursor = conn.cursor()

                placeholders = ','.join(['%s'] * len(intoColumns))
                query = f'INSERT INTO {intoSchema}.{intoTableName} ({", ".join(intoColumns)}) VALUES ({placeholders});'             
                cursor.execute(query, fromValues)  
                conn.commit()

                cursor.close()
                self.db.releaseConnection(conn)
                print("Put away a PostgreSQL connection")
        
        except Exception as e:
            print(e)

    def returnVisits(self):

        utilsInstance = Utils()

        previousVisits = utilsInstance.returnSqlData("dbo","vw_stadiumsVisited") 
        return previousVisits           
