import os
import sys

# Добавляем путь к директории app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

import pytest 

# Импортируем классы
from domain.entities.money import Money
from domain.value_objects.currency import Currency

from domain.exceptions.money import MoneyInvalidValue

def test_money_invalid_value():
    currency = Currency(1, 'USD', 'United States dollar', '$')
    
    with pytest.raises(MoneyInvalidValue, match='Amount of money cannot be negative'):
        money = Money(-10, currency)

if __name__ == "__main__":
    test_money_invalid_value()
