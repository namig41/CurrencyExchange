from application.router.base import BaseRouter
from application.http.response.http_response import HTTPResponse
from application.http.request.http_request import HTTPRequest

from infrastructure.dao.currencies import CurrenciesDAO

from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from application.http.response.exchange_rates_errors import ExchangeRatesNotFoundError

from application.http.response.currency_error import CurrencyNotFoundError

from application.http.response.base_success import SuccessResponse

class ExchangeRatesRouter(BaseRouter):

    def __init__(self):
        self.prefix = "exchangeRates"

        self.dao_exchange_rate = ExchangeRatesDAO()
        self.dao_currencies = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) != 1:
            return ExchangeRatesNotFoundError()

        exchange_rates = self.dao_exchange_rate.find_all()
        return SuccessResponse(exchange_rates)
        
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        
        from_currency = self.dao_currencies.find_by(code=request.body["baseCurrencyCode"][0])
        to_currency = self.dao_currencies.find_by(code=request.body["targetCurrencyCode"][0])

        if not from_currency:
            return CurrencyNotFoundError(request.body["baseCurrencyCode"][0])
        
        if not to_currency:
            return CurrencyNotFoundError(request.body["targetCurrencyCode"][0])
        
        exchange_rate_data = {
            "BaseCurrencyId": from_currency["id"],
            "TargetCurrencyId": to_currency["id"],
            "Rate": float(request.body["rate"][0])
        }

        self.dao_exchange_rate.insert(exchange_rate_data)

        exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
                                              TargetCurrencyId=to_currency["id"])
        
        exchange  = {
            "id": exchange_rate["id"],
            "baseCurrency": from_currency,
            "targetCurrency": to_currency,
            "rate": exchange_rate["rate"],
        }

        return SuccessResponse(exchange)

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
