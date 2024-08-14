from currencies.dao import CurrenciesDAO
from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse
from handlers.http_request import HTTPRequest

from exchange_rates.dao import ExchangeRatesDAO

from exchange_rate.errors import ExchangeRateNotFoundError, ExchangeRateMissingError


class ExchangeRateRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/exchangeRate"

        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) != 2:
            return ExchangeRateMissingError()

        from_currency, to_currency = request.parts[1][:3], request.parts[1][3:]

        from_currency_data = self.dao_currencies.find_by(code=from_currency)
        to_currency_data = self.dao_currencies.find_by(code=to_currency)


        if not from_currency_data:
            return ExchangeRateNotFoundError(from_currency)
        
        if not to_currency_data:
            return ExchangeRateNotFoundError(to_currency)
    
        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency_data["id"],
                                            TargetCurrencyId=to_currency_data["id"])

        if not exchange_rate:
            return ExchangeRateNotFoundError(to_currency)
         
        data  = {
            "id": exchange_rate["id"],
            "baseCurrency": from_currency_data,
            "targetCurrency": to_currency_data,
            "rate": exchange_rate["rate"],
        }

        return HTTPResponse(200, data)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            from_currency, to_currency = request.parts[1][:3], request.parts[1][3:]
            data = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency, TargetCurrencyId=to_currency)

            if not data:
                return ExchangeRateNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        return ExchangeRateNotFoundError()