from abc import abstractmethod
from typing import Protocol

from domain.entities.exchange_rate import ExchangeRate


class ICurrencyExchangeRateRepository(Protocol):

    @abstractmethod
    def get_exchange_rate_by_codes(
        self,
        base_code: str,
        target_code: str,
    ) -> ExchangeRate | None: ...
