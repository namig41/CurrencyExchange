from infrastructure.router.base import BaseRouter
from infrastructure.http.response.http_response import HTTPResponse
from infrastructure.http.request.http_request import HTTPRequest
from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.http.response.currency_error import (CurrencyNotFoundError,
                                                             CurrencyCodeMissingError,
                                                             RequiredFieldMissingError)

from infrastructure.http.response.base_success import SuccessResponse

class CurrencyRouter(BaseRouter):

    def __init__(self):
        self.prefix = "currency"
        self.dao = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) != 2:
            return RequiredFieldMissingError()
        
        currency_code = request.parts[1]

        if not currency_code:
            return CurrencyCodeMissingError()
        
        currency = self.dao.find_by(code=currency_code)
        if not currency:
            return CurrencyNotFoundError(currency_code)
        
        return SuccessResponse(currency)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
