from urllib.parse import unquote, urlparse, parse_qs
from pathlib import PurePosixPath


class HTTPRequest:
    def __init__(self, path='/'):
        self.path = path
        self.parts = []
        self.params = None
        self.body = None

    def __str__(self) -> str:
        return "path: {}, params: {}, body: {}".format(self.path, self.params, self.body)
    
    def parse(self):
        self.path = urlparse(self.path)
        self.param = parse_qs(self.path)
        self.parts = self.path.split('/')