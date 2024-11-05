from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


@dataclass
class BaseCurrenciesRepository(ABC):
    @abstractmethod
    def check_currency_exists_by_id(self, currency_id: int) -> bool: ...

    @abstractmethod
    def get_currencies(self) -> Iterable[Currency]: ...

    @abstractmethod
    def get_currency_by_id(self, currency_id: int) -> Currency | None: ...

    @abstractmethod
    def get_currency_by_code(self, currency_code: str) -> Currency | None: ...

    @abstractmethod
    def add_currency(self, currency: Currency) -> None: ...


@dataclass
class BaseExchangeRatesRepository(ABC):
    @abstractmethod
    def check_exchange_rate_exists_by_id(
        self,
        base_currency: Currency,
        target_currency: Currency,
    ) -> bool: ...

    @abstractmethod
    def get_exchange_rate_by_id(
        self,
        base_currency: Currency,
        target_currency: Currency,
    ) -> ExchangeRate | None: ...

    @abstractmethod
    def get_exchange_rate_by_codes(
        self,
        base_code: str,
        target_code: str,
    ) -> ExchangeRate | None: ...

    @abstractmethod
    def get_exchange_rates(self) -> Iterable[ExchangeRate]: ...

    @abstractmethod
    def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None: ...

    @abstractmethod
    def update_exchange_rate(self, exchange_rate: ExchangeRate) -> None: ...
