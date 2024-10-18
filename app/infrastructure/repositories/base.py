from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


@dataclass
class BaseCurrenciesRepository(ABC):
    @abstractmethod
    async def check_currency_exists_by_id(self, id: int) -> bool:
        ...

    @abstractmethod
    async def get_currencies(self) -> Iterable[Currency]:
        ...

    @abstractmethod
    async def get_currency_by_id(self, id: int) -> Currency | None:
        ...
     
    @abstractmethod
    async def add_currency(self, currency: Currency) -> None:
        ...

@dataclass
class BaseExchangeRatesRepository(ABC):
    @abstractmethod
    async def check_exchange_rate_exists_by_base_target_currency(self, base_currency: Currency, target_currency: Currency) -> bool:
        ...

    @abstractmethod
    async def get_exchange_rate_by_id(self, base_currency: Currency, target_currency: Currency) -> ExchangeRate | None:
        ...
     
    @abstractmethod
    async def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        ...