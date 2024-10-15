from dataclasses import dataclass

from domain.entities.base import BaseEntity
from domain.value_objects.currency import Currency

from domain.exceptions.money import MoneyInvalidValueException

@dataclass
class Money(BaseEntity):
    amount: float
    currency: Currency

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        if self.amount < 0:
            raise MoneyInvalidValueException()

    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency})"
