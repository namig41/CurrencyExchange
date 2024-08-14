from handlers.http_response import HTTPResponse

class ExchangeRatesMissingError(HTTPResponse):
    def __init__(self):
        super().__init__(400, {'error': 'Currency pair codes are missing in the request'})

class ExchangeRatesNotFoundError(HTTPResponse):
    def __init__(self):
        super().__init__(404, {'error': f'Exchange rate for pair not found'})
