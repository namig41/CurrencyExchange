from infrastructure.repositories.base import BaseExchangeRatesRepository

from domain.services.currency_exchange_service import (
    cross_exchange,
    exchange,
    reverse_exchange,
)


def test_exchange(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
):

    from_currency = "USD"
    to_currency = "EUR"

    _, converted_amount = exchange(
        from_currency,
        to_currency,
        10,
        exchange_rates_sqlite_repository,
    )

    assert converted_amount == 5


def test_reverse_exchange(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
):

    from_currency = "EUR"
    to_currency = "USD"

    _, converted_amount = reverse_exchange(
        from_currency,
        to_currency,
        10,
        exchange_rates_sqlite_repository,
    )

    assert converted_amount == 20


def test_cross_exchange(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
):

    from_currency = "EUR"
    to_currency = "AUD"

    _, converted_amount = cross_exchange(
        from_currency,
        to_currency,
        10,
        exchange_rates_sqlite_repository,
    )

    assert converted_amount == 10
