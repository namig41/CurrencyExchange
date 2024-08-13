import json

from currencies.dao import CurrenciesDAO
from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse
from handlers.http_request import HTTPRequest
from exchange_rates.dao import ExchangeRateDAO
from exchange_rates.errors import ExchangeRateNotFoundError, ExchangeRateMissingError


class ExchangeRateRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/exchangeRate"

        self.dao_exchange_rate = ExchangeRateDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            data = self.dao_exchange_rate.find_by(code=request.parts[1])
            if not data:
                return ExchangeRateNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        return ExchangeRateNotFoundError()

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            from_currency, to_currency = request.parts[1][:3], request.parts[1][3:]
            data = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency, TargetCurrencyId=to_currency)

            print(data)

            if not data:
                return ExchangeRateNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        return ExchangeRateNotFoundError()