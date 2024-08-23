from app.infrastructure.dao.base import DAO

class ExchangeRatesDAO(DAO):

    def __init__(self):
        super().__init__(table_name="ExchangeRates")
