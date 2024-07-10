import json

from currencies.dao import CurrenciesDAO
from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse
from handlers.http_request import HTTPRequest
from exchange_rates.dao import ExchangeRateDAO
from exchange_rates.errors import ExchangeRateNotFoundError, ExchangeRateMissingError


class ExchangeRatesRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/exchangeRates"

        self.dao_exchange_rate = ExchangeRateDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            data = self.dao_exchange_rate.find_by(code=request.parts[1])
            if not data:
                return ExchangeRateNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        if len(request.parts) == 1:
            data = self.dao_exchange_rate.find_all()
            return HTTPResponse(200, data)
        
        return ExchangeRateNotFoundError()

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:

        from_currency = self.dao_currencies.find_by(code=request.body["baseCurrencyCode"])
        to_currency = self.dao_currencies.find_by(code=request.body["targetCurrencyCode"])

        if not from_currency or not to_currency:
            return ExchangeRateNotFoundError()
        
        # ExchangeRates (ID, BaseCurrencyId, TargetCurrencyId, Rate)

        insert_data = {
            "BaseCurrencyId": from_currency["id"],
            "TargetCurrencyId": to_currency["id"],
            "Rate": float(request.body["rate"])
        }

        self.dao_exchange_rate.insert(insert_data)

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        data  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": exchange_rate["rate"],
        }

        return HTTPResponse(200, data)

    def handle_delete(self, request: HTTPRequest) -> HTTPResponse:
        pass