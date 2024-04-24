import psycopg2.pool
from config.Secrets import Secrets

class DatabasePool:
    def __init__(self):
        self.pool = None
        self.initializePool()

    def initializePool(self):
        SecretsInstance = Secrets()
        try:
            print("Connection pool created successfully")
            self.pool = psycopg2.pool.ThreadedConnectionPool(
                minconn=1,
                maxconn=2,
                database=SecretsInstance.postGreSqlDatabase,
                user=SecretsInstance.postGreSqlUser,
                password=SecretsInstance.postGreSqlPassword,
                host=SecretsInstance.postGreSqlHost,
                port=SecretsInstance.postGreSqlPort
            )
        except Exception as e:
            print(e)

    def getConnection(self):
        try:
            return self.pool.getconn()
        except Exception as e:
            print(e)

    def releaseConnection(self, conn):
        try:
            self.pool.putconn(conn)
        except Exception as e:
            print(e)

    def closeAllConnections(self):
        try:
            self.pool.closeall()
        except Exception as e:
            print(e)
