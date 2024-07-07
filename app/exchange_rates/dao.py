from dao.dao import DAO

class ExchangeRateDAO(DAO):

    def __init__(self):
        self.table_name = "exchange_rate"
