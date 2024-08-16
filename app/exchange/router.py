from exchange_rates.dao import ExchangeRatesDAO
from currencies.dao import CurrenciesDAO

from router.base import BaseRouter
from requestschema.http_response import HTTPResponse  
from requestschema.http_request import HTTPRequest

from exchange.errors import ExchangeNotFoundError

from currency.errors import (CurrencyNotFoundError,
                               CurrencyAlreadyExistsError,
                               DatabaseError,
                               RequiredFieldMissingError)

from response.base_success import SuccessResponse

class ExchangeRouter(BaseRouter):

    def __init__(self):
        self.prefix = "exchange"
        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:

        required_fields = ["from", "to", "amount"]
        missing_fields = [field for field in required_fields if field not in request.param]

        if missing_fields:
            return RequiredFieldMissingError()

        from_currency = self.dao_currencies.find_by(code=request.param["from"][0])
        to_currency = self.dao_currencies.find_by(code=request.param["to"][0])

        if not from_currency or not to_currency:
            return CurrencyNotFoundError()

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        if not exchange_rate:
            return ExchangeNotFoundError()

        converted_amount = exchange_rate["rate"] * int(request.param["amount"][0])

        exchange  = {"baseCurrency": from_currency,
                 "targetCurrency": to_currency,
                 "rate": exchange_rate["rate"],
                 "amount": request.param["amount"][0],
                 "convertedAmount": converted_amount
        }

        return SuccessResponse(exchange)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass