from dao.dao import DAO

class CurrencyDAO(DAO):
    
    def __init__(self):
        super().__init__(table_name="currencies")