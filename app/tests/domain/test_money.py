import pytest 

from domain.entities.money import Money
from domain.exceptions.money import MoneyInvalidValueException
from domain.value_objects.currency import Currency

def test_money_invalid_value():
    currency = Currency(1, 'USD', 'United States dollar', '$')
    
    with pytest.raises(MoneyInvalidValueException):
        money = Money(-10, currency)
