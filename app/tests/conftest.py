import pytest
from pytest_asyncio import fixture

from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.memory import MemoryCurrenciesRepository
from infrastructure.repositories.sqlite import sqlite_currencies_repository_factory, sqlite_exchange_rates_repository_factory


@fixture
def currency_memory_repository() -> BaseCurrenciesRepository:
    return MemoryCurrenciesRepository()

@fixture
def currencies_sqlite_repository() -> BaseCurrenciesRepository:
    return sqlite_currencies_repository_factory()

@fixture
def exchange_rates_sqlite_repository() -> BaseExchangeRatesRepository:
    return sqlite_exchange_rates_repository_factory()