from typing import Iterable
from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate


def convert_currency_entity_to_document(currency: Currency) -> dict:
    return {
        'id': currency.id,
        'code': currency.code,
        'fullname': currency.fullname,
        'sign': currency.sign,
    }
    
def convert_currency_document_to_entity(currency_data: dict) -> Currency:
    return Currency(
        id=currency_data['id'],
        code=currency_data['code'],
        fullname=currency_data['fullname'],
        sign=currency_data['sign'],
    )
    
def convert_exchange_rate_entity_to_document(exchange_rate: ExchangeRate) -> dict:
    return {
        'id': exchange_rate.id,
        'basecurrencyid': exchange_rate.base_currency.id,
        'targetcurrencyid': exchange_rate.target_currency.id,
        'rate': exchange_rate.rate,
    }
    
def convert_exchange_rate_document_to_entity(exchange_rate_data: dict,
                                             base_currency: Currency, 
                                             target_currency: Currency) -> ExchangeRate:
    return ExchangeRate(
        id=exchange_rate_data['id'],
        base_currency=base_currency,
        target_currency=target_currency,
        rate=exchange_rate_data['rate'],
    )
    
    
def convert_exchange_rates_document_to_entity(exchange_rates_data: list[dict]) -> Iterable[ExchangeRate]:
    
    exchange_rates: list[ExchangeRate] = []
    
    for exchange_rate_data in exchange_rates_data:
        base_currency = Currency(id=exchange_rate_data['baseid'],
                               code=exchange_rate_data['basecode'],
                               fullname=exchange_rate_data['basefullname'],
                               sign=exchange_rate_data['basesign'])
         
        target_currency = Currency(id=exchange_rate_data['targetid'],
                                code=exchange_rate_data['targetcode'],
                                fullname=exchange_rate_data['targetfullname'],
                                sign=exchange_rate_data['targetsign'])
        
        exchange_rates.append(ExchangeRate(id=exchange_rate_data['id'],
                                           base_currency=base_currency,
                                           target_currency=target_currency,
                                           rate=exchange_rate_data['rate']))
        
    return exchange_rates


def convert_exchange_rates_entity_to_document(exchange_rates: list[ExchangeRate]) -> list[dict]:
    
    exchange_rates_data: list[dict] = []
    
    for exchange_rate in exchange_rates:
        exchange_rates_data.append({
                "id": exchange_rate.id,
                "baseCurrency": {
                    "id": exchange_rate.base_currency.id,
                    "name": exchange_rate.base_currency.fullname,
                    "code": exchange_rate.base_currency.code,
                    "sign": exchange_rate.base_currency.sign
                },
                "targetCurrency": {
                    "id": exchange_rate.target_currency.id,
                    "name": exchange_rate.target_currency.fullname,
                    "code": exchange_rate.target_currency.code,
                    "sign": exchange_rate.target_currency.sign
                },
                "rate": exchange_rate.rate.value,
            }
        )
        
    return exchange_rates_data