import json

from exchange_rates.dao import ExchangeRateDAO
from currencies.dao import CurrenciesDAO

from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse  
from handlers.http_request import HTTPRequest

from exchange.errors import CurrencyNotFoundError

class ExchangeRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/exchange"
        self.dao_exchange_rate = ExchangeRateDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:

        from_currency = self.dao_currencies.find_by(code=request.param["from"][0])
        to_currency = self.dao_currencies.find_by(code=request.param["to"][0])

        if not from_currency or not to_currency:
            return CurrencyNotFoundError()

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        converted_amount = exchange_rate["rate"] * int(request.param["amount"][0])

        data  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": exchange_rate["rate"],
                 "amount": request.param["amount"][0],
                 "convertedAmount": converted_amount
        }

        return HTTPResponse(200, data)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_delete(self, request: HTTPRequest) -> HTTPResponse:
        pass