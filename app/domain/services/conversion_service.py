from app.domain.entities.currency import Currency
from app.domain.value_objects.money import Money


class ConversionService:

    def convert(self, from_money: Money, to_currency: Currency, rate: float) -> Money:
        if from_money.currency == to_currency:
            return from_money
        return Money(from_money.amount * rate, to_currency)
