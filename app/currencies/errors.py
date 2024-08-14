from handlers.http_response import HTTPResponse

class CurrencyNotFoundError(HTTPResponse):
    def __init__(self, currency_code):
        super().__init__(404, {'error': f'Currency "{currency_code}" not found'})

class CurrencyCodeMissingError(HTTPResponse):
    def __init__(self):
        super().__init__(400, {'error': 'Currency code is missing in the request'})

class RequiredFieldMissingError(HTTPResponse):
    def __init__(self):
        super().__init__(400, {'error': f'Required field is missing'})

class CurrencyAlreadyExistsError(HTTPResponse):
    def __init__(self):
        super().__init__(409, {'error': f'Currency with code already exists'})

class DatabaseError(HTTPResponse):
    def __init__(self, error_message):
        super().__init__(500, {'error': error_message})