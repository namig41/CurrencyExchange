from typing import Iterable
import pytest

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository

@pytest.mark.asyncio
async def test_add_currency_in_repository(currencies_sqlite_repository: BaseCurrenciesRepository):
    
    currency: Currency  = Currency('AZN', 'Azerbaijani manat', '₼', id=4)
    await currencies_sqlite_repository.add_currency(currency)
    currency_returned: Currency = await currencies_sqlite_repository.get_currency_by_id(currency.id)
    assert currency_returned == currency
    
@pytest.mark.asyncio
async def test_get_currencies_in_repository(currencies_sqlite_repository: BaseCurrenciesRepository):
    
    currenices: Iterable[Currency] = await currencies_sqlite_repository.get_currencies()
    
    assert len(currenices) != []
    
@pytest.mark.asyncio
async def test_add_exchange_rate_in_repository(
    exchange_rates_sqlite_repository: BaseExchangeRatesRepository,
    currencies_sqlite_repository: BaseCurrenciesRepository):
    
    base_currency: Currency  = await currencies_sqlite_repository.get_currency_by_id(id=2)
    target_currency: Currency  = await currencies_sqlite_repository.get_currency_by_id(id=3)
    
    exchange_rate = ExchangeRate(base_currency=base_currency, target_currency=target_currency, rate=0.5, id=3)
    
    await exchange_rates_sqlite_repository.add_exchange_rate(exchange_rate)
    
    exchange_rate_returned: ExchangeRate = await exchange_rates_sqlite_repository.get_exchange_rate_by_id(base_currency, target_currency)
    
    assert exchange_rate_returned == exchange_rate     