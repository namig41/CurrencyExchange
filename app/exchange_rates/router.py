from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse
from handlers.http_request import HTTPRequest

from currencies.dao import CurrenciesDAO

from exchange_rates.dao import ExchangeRatesDAO
from exchange_rates.errors import ExchangeRatesNotFoundError, ExchangeRatesMissingError


class ExchangeRatesRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/exchangeRates"

        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 1:
            data = self.dao_exchange_rate.find_all()
            return HTTPResponse(200, data)
        
        return ExchangeRatesNotFoundError()

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        from_currency = self.dao_currencies.find_by(code=request.body["baseCurrencyCode"][0])
        to_currency = self.dao_currencies.find_by(code=request.body["targetCurrencyCode"][0])

        if not from_currency:
            return ExchangeRatesNotFoundError(request.body["baseCurrencyCode"][0])
        
        if not to_currency:
            return ExchangeRatesNotFoundError(request.body["targetCurrencyCode"][0])
        
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
        pass