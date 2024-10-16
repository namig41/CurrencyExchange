import pytest 

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.exchange_rate import EqualCurrencyException
from domain.value_objects.rate import Rate

def test_exchange_rate_invalid_value():
    currency = Currency('USD', 'United States dollar', '$')
    
    
    with pytest.raises(EqualCurrencyException):
        ExchangeRate(currency, currency, Rate(10.))
