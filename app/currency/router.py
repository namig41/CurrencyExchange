import json

from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse  
from handlers.http_request import HTTPRequest
from currency.dao import CurrencyDAO
from currency.errors import CurrencyNotFoundError, CurrencyCodeMissingError, DatabaseError


class CurrencyRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/currency"
        self.dao = CurrencyDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            data = self.dao.find_by(code=request.parts[1])
            if not data:
                return CurrencyNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        else:
            return CurrencyCodeMissingError()
        
        return DatabaseError()

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass