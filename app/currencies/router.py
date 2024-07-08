import json

from handlers.base_router import BaseRouter
from currencies.dao import CurrenciesDAO

class CurrenciesRouter(BaseRouter):

    def __init__(self):

        self.prefix = "/currencies"
        self.dao = CurrenciesDAO()

    def handle_get(self, request):
        return 200, {"1":1, "2":2 }

    def handle_post(self, request):
        if self.path == self.prefix:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            response = {'received': data}
            self._set_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found')

    def handle_delete(self):
        if self.path == self.prefix:
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Data deleted'}).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found') 