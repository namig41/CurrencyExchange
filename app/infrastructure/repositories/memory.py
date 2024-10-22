from dataclasses import dataclass, field
from typing import Iterable

from domain.entities.currency import Currency
from infrastructure.repositories.base import BaseCurrenciesRepository


@dataclass
class MemoryCurrenciesRepository(BaseCurrenciesRepository):
    
    _saved_currencies: set[Currency] = field(
        default_factory=set,
        kw_only=True,
    )
    
    async def check_currency_exists_by_id(self, id: int) -> bool:
        try:
            return bool(
                next(
                    currency for currency in self._saved_currencies if currency.id == id
                )
            )
        except StopIteration:
            return False
        
    async def get_currencies(self) -> Iterable[Currency]:
        return self._saved_currencies
        
    async def get_currency_by_id(self, id: int) -> Currency | None:
        try:
            return next(
                    currency for currency in self._saved_currencies if currency.id == id
                )
        except StopIteration:
            return False
        
    async def get_currency_by_code(self, code: str) -> Currency | None:
        try:
            return next(
                    currency for currency in self._saved_currencies if currency.code == code
                )
        except StopIteration:
            return False
     
    async def add_currency(self, currency: Currency) -> None:
        self._saved_currencies.add(currency)