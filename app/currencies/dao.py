from dao.dao import DAO

class CurrenciesDAO(DAO):
    
    def __init__(self):
        super().__init__(table_name="currencies")