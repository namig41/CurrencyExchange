import pytest

from domain.entities.currency import Currency
from infrastructure.repositories.base import BaseCurrenciesRepository

@pytest.mark.asyncio
async def test_add_currency_in_repository(currency_memory_repository: BaseCurrenciesRepository):
    
    currency: Currency  = Currency('USD', 'United States dollar', '$')
    await currency_memory_repository.add_currency(currency)
    currency_returned: Currency = await currency_memory_repository.get_currency_by_id(currency.id)
    
    assert currency_returned == currency     