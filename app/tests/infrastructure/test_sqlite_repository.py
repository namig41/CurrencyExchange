from decimal import Decimal
from typing import Iterable

from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.value_objects.rate import Rate


def test_add_currency_in_repository(
    currencies_sqlite_repository: BaseCurrenciesRepository,
):

    currency: Currency = Currency("AZN", "Azerbaijani manat", "₼", id=4)

    currencies_sqlite_repository.add_currency(currency)
    currency_returned: Currency = currencies_sqlite_repository.get_currency_by_code(
        currency.code,
    )
    assert currency_returned == currency


def test_get_currencies_in_repository(
    currencies_sqlite_repository: BaseCurrenciesRepository,
):
    currenices: Iterable[Currency] = currencies_sqlite_repository.get_currencies()
    assert currenices != []


def test_add_exchange_rate_in_repository(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
    currencies_sqlite_repository: BaseCurrenciesRepository,
):

    base_currency: Currency = currencies_sqlite_repository.get_currency_by_id(
        currency_id=2,
    )
    target_currency: Currency = currencies_sqlite_repository.get_currency_by_id(
        currency_id=3,
    )

    exchange_rate = ExchangeRate(
        base_currency=base_currency,
        target_currency=target_currency,
        rate=Rate(Decimal(0.5)),
        id=3,
    )

    exchange_rates_sqlite_repository.add_exchange_rate(exchange_rate)

    exchange_rate_returned: ExchangeRate = (
        exchange_rates_sqlite_repository.get_exchange_rate_by_id(
            base_currency,
            target_currency,
        )
    )

    assert exchange_rate_returned == exchange_rate


def test_get_exchange_rates_in_repository(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
):

    exchange_rate_returned: Iterable[ExchangeRate] = (
        exchange_rates_sqlite_repository.get_exchange_rates()
    )

    assert exchange_rate_returned != []
