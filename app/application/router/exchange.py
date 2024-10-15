from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from infrastructure.dao.currencies import CurrenciesDAO

from infrastructure.router.base import BaseRouter
from infrastructure.http.response.http_response import HTTPResponse
from infrastructure.http.request.http_request import HTTPRequest

from infrastructure.http.response.exchange_errors import ExchangeNotFoundError

from infrastructure.http.response.currency_error import (CurrencyNotFoundError,
                                                             RequiredFieldMissingError)

from infrastructure.http.response.base_success import SuccessResponse

class ExchangeRouter(BaseRouter):

    def __init__(self):
        self.prefix = "exchange"
        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def forward_convert(self, request: HTTPRequest):
        from_currency = self.dao_currencies.find_by(code=request.param["from"][0])
        to_currency = self.dao_currencies.find_by(code=request.param["to"][0])

        if not from_currency or not to_currency:
            return

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        if not exchange_rate:
            return

        converted_amount = exchange_rate["rate"] * float(request.param["amount"][0])

        exchange  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": exchange_rate["rate"],
                 "amount": request.param["amount"][0],
                 "convertedAmount": converted_amount
        }

        return SuccessResponse(exchange)
    

    def reverse_convert(self, request: HTTPRequest):

        from_currency = self.dao_currencies.find_by(code=request.param["to"][0])
        to_currency = self.dao_currencies.find_by(code=request.param["from"][0])

        if not from_currency or not to_currency:
            return

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        if not exchange_rate:
            return 

        converted_amount = exchange_rate["rate"] * 1 / float(request.param["amount"][0])

        exchange  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": exchange_rate["rate"],
                 "amount": request.param["amount"][0],
                 "convertedAmount": converted_amount
        }

        return SuccessResponse(exchange)
    

    def cross_convert(self, request: HTTPRequest):

        from_currency = self.dao_currencies.find_by(code=request.param["to"][0])
        to_usd_currency = self.dao_currencies.find_by(code="USD")
        to_currency = self.dao_currencies.find_by(code=request.param["from"][0])

        if not from_currency or not to_currency:
            return CurrencyNotFoundError()

        exchange_rate_1 = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_usd_currency["id"])
        
        exchange_rate_2 = self.dao_exchange_rate.find_by(BaseCurrencyId=to_usd_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        if not exchange_rate_1 or not exchange_rate_2:
            return ExchangeNotFoundError()

        converted_amount = exchange_rate_1["rate"] * float(request.param["amount"][0])
        converted_amount = exchange_rate_2["rate"] * float(converted_amount)

        exchange  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": {exchange_rate_1["rate"], exchange_rate_2["rate"]},
                 "amount": request.param["amount"][0],
                 "convertedAmount": converted_amount
        }

        return SuccessResponse(exchange)

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:

        required_fields = ["from", "to", "amount"]
        missing_fields = [field for field in required_fields if field not in request.param]

        if missing_fields:
            return RequiredFieldMissingError()

        return (self.forward_convert(request) or
                self.reverse_convert(request) or
                self.cross_convert(request) or
                ExchangeNotFoundError())
    
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
