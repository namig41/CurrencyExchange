import json

from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse  
from handlers.http_request import HTTPRequest
from currencies.dao import CurrenciesDAO
from currencies.errors import CurrencyNotFoundError


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
        if request.parts:
            self.dao.insert(request.body["baseCurrencyCode"], )
            return HTTPResponse(200, "Успешно")

        return HTTPResponse(200, "Успешно")

    def handle_delete(self):
        if self.path == self.prefix:
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Data deleted'}).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found') 