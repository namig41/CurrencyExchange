from dataclasses import dataclass

@dataclass
class ExchangeRate:
    id: int
    from_currency: str
    to_currency: str
    rate: float
