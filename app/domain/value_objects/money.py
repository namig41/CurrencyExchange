from dataclasses import dataclass

from app.domain.entities.currency import Currency


@dataclass(frozen=True)
class Money:
    amount: float
    currency: Currency