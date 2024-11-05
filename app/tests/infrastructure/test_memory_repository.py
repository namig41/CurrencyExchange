from infrastructure.repositories.base import BaseCurrenciesRepository

from domain.entities.currency import Currency


def test_add_currency_in_repository(
    currency_memory_repository: BaseCurrenciesRepository,
):

    currency: Currency = Currency("USD", "United States dollar", "$")
    currency_memory_repository.add_currency(currency)
    currency_returned: Currency = currency_memory_repository.get_currency_by_id(
        currency.id,
    )

    assert currency_returned == currency
