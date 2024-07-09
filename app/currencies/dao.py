from dao.dao import DAO

from storage.sqlite import SQLiteDatabase

class CurrenciesDAO(DAO):
    
    def __init__(self):
        self.table_name = "currencies"

        self.database = SQLiteDatabase()
        self.database.connect()
        self.database.init()