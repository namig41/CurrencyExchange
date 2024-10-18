from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


def convert_currency_entity_to_document(currency: Currency) -> dict:
    return {
        'id': currency.id,
        'code': currency.code,
        'fullname': currency.fullname,
        'sign': currency.sign,
    }
    
def convert_currency_document_to_entity(currency: dict) -> Currency:
    return Currency(
        id=currency['id'],
        code=currency['code'],
        fullname=currency['fullname'],
        sign=currency['sign'],
    )
    
def convert_exchange_rate_entity_to_document(exchange_rate: ExchangeRate) -> dict:
    return {
        'id': exchange_rate.id,
        'basecurrencyid': exchange_rate.base_currency.id,
        'targetcurrencyid': exchange_rate.target_currency.id,
        'rate': exchange_rate.rate,
    }
    
def convert_exchange_rate_document_to_entity(exchange_rate: dict,
                                             base_currency: Currency, 
                                             target_currency: Currency) -> ExchangeRate:
    return ExchangeRate(
        id=exchange_rate['id'],
        base_currency=base_currency,
        target_currency=target_currency,
        rate=exchange_rate['rate'],
    )