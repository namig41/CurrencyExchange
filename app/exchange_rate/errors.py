from handlers.http_response import HTTPResponse

class ExchangeRateMissingError(HTTPResponse):
    def __init__(self):
        super().__init__(400, {'error': 'Currency pair codes are missing in the request'})

class ExchangeRateNotFoundError(HTTPResponse):
    def __init__(self, currency_pair):
        super().__init__(404, {'error': f'Exchange rate for pair "{currency_pair}" not found'})
