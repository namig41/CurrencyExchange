from handlers.http_response import HTTPResponse

class CurrencyNotFoundError(HTTPResponse):
    def __init__(self):
        super().__init__(404, {'message': f'Currency not found'})