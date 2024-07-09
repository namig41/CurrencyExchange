import json

from handlers.base_router import BaseRouter
from handlers.http_response import HTTPResponse  
from handlers.http_request import HTTPRequest
from currencies.dao import CurrenciesDAO

from pathlib import PurePosixPath

class CurrenciesRouter(BaseRouter):

    def __init__(self):

        self.prefix = "/currencies"
        self.dao = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:

        print(request.parts)

        if path:
            data = self.dao.find_all()
        else:
            data = self.dao.find_by_name(cur_code)
        
        response = HTTPResponse(200, data)
        return response

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:


        return HTTPResponse(200, "Успешно")

    def handle_delete(self):
        if self.path == self.prefix:
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Data deleted'}).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found') 