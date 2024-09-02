from infrastructure.dao.base import DAO

class ExchangeRatesDAO(DAO):

    def __init__(self) -> None:
        super().__init__(table_name="ExchangeRates")
