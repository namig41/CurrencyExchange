from http.server import BaseHTTPRequestHandler
import json
from abc import ABC, abstractmethod

class BaseRouter(BaseHTTPRequestHandler, ABC):

    def __init__(self):
        self.prefx = None

    def _set_headers(self, content_type='application/json', status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    @abstractmethod
    def handle_get(self):
        pass

    @abstractmethod
    def handle_post(self):
        pass

    @abstractmethod
    def handle_put(self):
        pass

    @abstractmethod
    def handle_delete(self):
        pass

    def do_GET(self):
        self.handle_get()

    def do_POST(self):
        self.handle_post()

    def do_PUT(self):
        self.handle_put()

    def do_DELETE(self):
        self.handle_delete()