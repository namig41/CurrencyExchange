from domain.entities.currency import Currency


def convert_currency_entity_to_document(currency: Currency) -> dict:
    return {
        'id': currency.id,
        'code': currency.code,
        'FullName': currency.fullname,
        'Sign': currency.sign,
    }
    
def convert_currency_document_to_entity(currency: dict) -> Currency:
    return Currency(
        id=currency['id'],
        code=currency['code'],
        fullname=currency['FullName'],
        sign=currency['Sign'],
    )