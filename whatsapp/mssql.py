import pymssql
from config import MSSQLConfig


class MSSQL():
    def __init__(self):
        config = MSSQLConfig()
        self.host = config.DB_HOST
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD
        self.db = config.DB_NAME
        self.conexion = pymssql.connect(
            self.host, self.user, self.password, self.db)
        self.conexion.close()
