import pytest
from pytest_asyncio import fixture

from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.memory import MemoryCurrenciesRepository


@fixture
def currency_repository() -> BaseCurrenciesRepository:
    return MemoryCurrenciesRepository()