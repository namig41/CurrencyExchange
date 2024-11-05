from http.server import HTTPServer
from threading import Thread

import pytest
from infrastructure.database.base import BaseDatabase
from infrastructure.database.sqlite import sqlite_database_factory
from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)
from infrastructure.repositories.memory import MemoryCurrenciesRepository
from infrastructure.repositories.sqlite import (
    sqlite_currencies_repository_factory,
    sqlite_exchange_rates_repository_factory,
)
from pytest_asyncio import fixture

from application.api.handler import HTTPHandler


@fixture
def currency_memory_repository() -> BaseCurrenciesRepository:
    return MemoryCurrenciesRepository()


@fixture
def currencies_sqlite_repository() -> BaseCurrenciesRepository:
    return sqlite_currencies_repository_factory()


@fixture
def exchange_rates_sqlite_repository() -> BaseExchangeRatesRepository:
    return sqlite_exchange_rates_repository_factory()


@fixture
def sqlite_database() -> BaseDatabase:
    return sqlite_database_factory()


@pytest.fixture(scope="module")
def http_server():
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, HTTPHandler)

    # Запускаем сервер в отдельном потоке
    thread = Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()

    yield httpd  # Возвращаем объект сервера для использования в тесте

    httpd.shutdown()
    thread.join()
