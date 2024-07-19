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
        from_currency = self.dao_currencies.find_by(code=request.body["baseCurrencyCode"][0])
        to_currency = self.dao_currencies.find_by(code=request.body["targetCurrencyCode"][0])

        if not from_currency:
            return ExchangeRateNotFoundError(request.body["baseCurrencyCode"][0])
        
        if not to_currency:
            return ExchangeRateNotFoundError(request.body["targetCurrencyCode"][0])
        
        insert_data = {
            "BaseCurrencyId": from_currency["id"],
            "TargetCurrencyId": to_currency["id"],
            "Rate": float(request.body["rate"][0])
        }

        self.dao_exchange_rate.insert(insert_data)

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        data  = {
            "id": exchange_rate["id"],
            "baseCurrency": from_currency,
            "targetCurrency": to_currency,
            "rate": exchange_rate["rate"],
        }

        return HTTPResponse(200, data)

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            from_currency, to_currency = request.parts[1][:3], request.parts[1][3:]
            data = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency, TargetCurrencyId=to_currency)

            print(data)

            if not data:
                return ExchangeRateNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        return ExchangeRateNotFoundError()