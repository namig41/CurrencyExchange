import pytest

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.exchange_rate import EqualCurrencyException
from domain.value_objects.rate import Rate


def test_exchange_rate_init_value():
    base_currency = Currency("USD", "United States dollar", "$")
    target_currency = Currency("EUR", "Euro", "€")

    exchange_rate = ExchangeRate(base_currency, target_currency, Rate(0.5))

    assert exchange_rate.base_currency == base_currency
    assert exchange_rate.target_currency == target_currency
    assert exchange_rate.rate.value == 0.5
    assert exchange_rate.rate.inverted == 2


def test_exchange_rate_invalid_value():
    currency = Currency("USD", "United States dollar", "$")

    with pytest.raises(EqualCurrencyException):
        ExchangeRate(currency, currency, Rate(10.0))
