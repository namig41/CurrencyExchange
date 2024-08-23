from dataclasses import dataclass

from app.domain.entities.currency import Currency


@dataclass
class Money:
    amount: float
    currency: Currency