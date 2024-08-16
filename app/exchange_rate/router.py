from router.base import BaseRouter

from currencies.dao import CurrenciesDAO
from requestschema.http_response import HTTPResponse
from requestschema.http_request import HTTPRequest

from exchange_rates.dao import ExchangeRatesDAO

from exchange_rate.errors import ExchangeRateNotFoundError, ExchangeRateMissingError, RequiredFieldMissingError

from response.base_success import SuccessResponse

class ExchangeRateRouter(BaseRouter):

    def __init__(self):
        self.prefix = "exchangeRate"

        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) != 2:
            return ExchangeRateMissingError()

        currency_pair =  request.parts[1]

        from_currency_code, to_currency_code = currency_pair[:3], currency_pair[3:]

        from_currency = self.dao_currencies.find_by(code=from_currency_code)
        to_currency = self.dao_currencies.find_by(code=to_currency_code)

        if not from_currency:
            return ExchangeRateNotFoundError(from_currency_code)
        
        if not to_currency:
            return ExchangeRateNotFoundError(to_currency_code)
    
        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                            TargetCurrencyId=to_currency["id"])

        if not exchange_rate:
            return ExchangeRateNotFoundError(currency_pair)
         
        exchange = {
            "id": exchange_rate["id"],
            "baseCurrency": from_currency,
            "targetCurrency": to_currency,
            "rate": exchange_rate["rate"],
        }

        return SuccessResponse(exchange)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) != 2:
            return RequiredFieldMissingError()
        
        currency_pair =  request.parts[1]

        from_currency, to_currency = currency_pair[:3], currency_pair[3:]
        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency, TargetCurrencyId=to_currency)

        if not exchange_rate:
            return ExchangeRateNotFoundError(currency_pair)
        
        return SuccessResponse(exchange_rate)
        
        