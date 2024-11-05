from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from infrastructure.database.base import BaseDatabase


def test_currencies_dao_init(sqlite_database: BaseDatabase):
    currencies_dao = CurrenciesDAO(database=sqlite_database)

    assert currencies_dao.table_name == "currencies"

    currency_data = currencies_dao.find_by_id(item_id=1)

    assert currency_data == {
        "id": 1,
        "code": "USD",
        "fullname": "United States dollar",
        "sign": "$",
    }


def test_exchange_rates_dao_init(sqlite_database: BaseDatabase):
    exchange_rates_dao = ExchangeRatesDAO(database=sqlite_database)

    assert exchange_rates_dao.table_name == "ExchangeRates"

    exchange_rate_data = exchange_rates_dao.find_by_id(item_id=1)

    assert exchange_rate_data == {
        "id": 1,
        "basecurrencyid": 1,
        "targetcurrencyid": 2,
        "rate": 0.5,
    }
