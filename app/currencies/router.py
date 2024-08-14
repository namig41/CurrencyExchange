import json

from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse  
from handlers.http_request import HTTPRequest
from currencies.dao import CurrenciesDAO
from currencies.errors import CurrencyNotFoundError, CurrencyAlreadyExistsError, RequiredFieldMissingError


class CurrenciesRouter(BaseRouter):

    def __init__(self):
        self.prefix = "/currencies"
        self.dao = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        if len(request.parts) == 2:
            data = self.dao.find_by(code=request.parts[1])
            if not data:
                return CurrencyNotFoundError(request.parts[1])
            return HTTPResponse(200, data)
        
        if len(request.parts) == 1:
            data = self.dao.find_all()
            return HTTPResponse(200, data)
        
        return CurrencyNotFoundError()

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        if request.body:

            if "name" in request.body and "code" in request.body and "sign" in request.body:
                insert_data = {
                    "FullName": request.body["name"][0],
                    "Code": request.body["code"][0],
                    "Sign": request.body["sign"][0]
                }

                data = self.dao.find_by(code=insert_data["Code"])
                if not data:
                    self.dao.insert(insert_data)
                    data = self.dao.find_by(code=insert_data["Code"])
                else:
                    return CurrencyAlreadyExistsError()
            else:
                return RequiredFieldMissingError()
            
            return HTTPResponse(200, data)

        return CurrencyNotFoundError()

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass