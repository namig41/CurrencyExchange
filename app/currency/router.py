from router.base import BaseRouter
from requestschema.http_response import HTTPResponse  
from requestschema.http_request import HTTPRequest
from currency.dao import CurrencyDAO
from currency.errors import (CurrencyNotFoundError,
                             CurrencyCodeMissingError,
                             RequiredFieldMissingError,
                             DatabaseError)

from response.base_success import SuccessResponse

class CurrencyRouter(BaseRouter):

    def __init__(self):
        self.prefix = "currency"
        self.dao = CurrencyDAO()

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