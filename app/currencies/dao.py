from dao.dao import DAO

class CurrenciesDAO(DAO):
    
    def __init__(self):
        self.table_name = "currencies"