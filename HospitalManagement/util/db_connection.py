import pyodbc
from util.property_util import PropertyUtil

class DBConnection:

    @staticmethod
    def getConnection():
        try:
            properties=PropertyUtil.getPropertyString()
            connection=pyodbc.connect(**properties)
            return connection
        except Exception as e:
            print(str(e) + '--Database is not connected--')
            return None