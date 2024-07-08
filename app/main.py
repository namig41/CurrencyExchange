from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

from currencies.router import CurrenciesRouter
from exchange_rates.router import ExchangeRatesRouter
from handlers.http_request import HTTPRequest

class SimpleHandler(BaseHTTPRequestHandler):

    http_code, message = 500, {'message': 'The server is in its initial state'}

    routers = [
        CurrenciesRouter(),
        ExchangeRatesRouter()
    ]

    def _set_headers(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):

        request = HTTPRequest()
        request.path = self.path
        request.param = self.get_query()
        
        for router in self.routers:
            if self.path.startswith(router.prefix):
                self.http_code, self.message = router.handle_get(request)
                break

        self.do_response()



    def do_POST(self):
        request = HTTPRequest()
        request.path = self.path

        content = None
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
           content = self.rfile.read(content_length)
        if content:
             request.data = json.loads(content.decode('utf-8'))

        for router in self.routers:
            if self.path.startswith(router.prefix):
                self.http_code, self.message = router.handle_post(request)
                break

        self.do_response()

    def do_response(self):
        # Sent response's header
        self.send_response(self.http_code)
        self.send_header("Content-type", 'text/json')
        self.end_headers()
        # Sent response's body
        response_content = json.dumps(self.message)
        self.wfile.write(response_content.encode())
    
    def get_query(self):
        parsed_url = urlparse(self.path)
        return parse_qs(parsed_url.query)
    
def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер начал работу {port}...')
    httpd.serve_forever()



if __name__ == "__main__":
    run()
