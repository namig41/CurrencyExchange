from handlers.base_router import BaseRouter
import json

class ExchengaRatesRouter(BaseRouter):

    def __init__(self):
        self.prefix = '/currencies'

    def handle_get(self):
        if self.path == self.prefix:
            data = {'message': 'Hello, world!'}
            self._set_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found')

    def handle_post(self):
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

    def handle_put(self):
        self.handle_post()

    def handle_delete(self):
        if self.path == self.prefix:
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Data deleted'}).encode('utf-8'))
        else:
            self._set_headers('text/html', 404)
            self.wfile.write(b'Not Found')