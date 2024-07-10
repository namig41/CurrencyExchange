from dao.dao import DAO

from storage.sqlite import SQLiteDatabase

class CurrenciesDAO(DAO):
    
    def __init__(self):
        super().__init__(table_name="currencies")