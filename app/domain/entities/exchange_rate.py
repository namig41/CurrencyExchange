from dataclasses import (
    dataclass,
    field,
)
from itertools import count

from domain.entities.base import BaseEntity
from domain.entities.currency import Currency
from domain.exceptions.exchange_rate import EqualCurrencyException
from domain.value_objects.rate import Rate


@dataclass
class ExchangeRate(BaseEntity):
    id: int = field(  # noqa: A003
        default_factory=count().__next__,
        kw_only=True,
    )
    base_currency: Currency
    target_currency: Currency
    rate: Rate

    def validate(self):
        if self.base_currency == self.target_currency:
            raise EqualCurrencyException()

    def __eq__(self, other: "ExchangeRate") -> bool:
        return (
            self.base_currency == other.base_currency
            and self.target_currency == other.target_currency
        )
