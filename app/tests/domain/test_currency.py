from domain.entities.currency import Currency


def test_currency_value():
    currency = Currency("USD", "United States dollar", "$")

    assert currency.code == "USD"
    assert currency.fullname == "United States dollar"
    assert currency.sign == "$"
