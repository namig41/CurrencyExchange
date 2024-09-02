from dataclasses import dataclass

from domain.value_objects.currency import Currency

from domain.exceptions.money import MoneyInvalidValue

@dataclass
class Money:
    amount: float
    currency: Currency

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        if self.amount < 0:
            raise MoneyInvalidValue("Amount of money cannot be negative")

    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency})"
