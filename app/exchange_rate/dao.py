from dao.dao import DAO

class ExchangeRateDAO(DAO):

    def __init__(self):
        super().__init__(table_name="ExchangeRates")
