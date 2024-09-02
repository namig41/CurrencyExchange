import os
import sys

# Добавляем путь к директории app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

# Импортируем классы
from domain.entities.money import Money
from domain.value_objects.currency import Currency
from domain.aggregates.exchange_rate import ExchangeRate

def test_forward_convert():
    base_currency = Currency(1, 'USD', 'United States dollar', '$')
    target_currency = Currency(2, 'EUR', 'Euro', '€')

    exchange_rate = ExchangeRate(1, base_currency, target_currency, 2)

    money = Money(3, base_currency)
    result = exchange_rate.forward_convert(money).amount

    assert result == 6, f'Expected 6 but got {result}'

if __name__ == "__main__":
    test_forward_convert()
