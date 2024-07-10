from urllib.parse import unquote, urlparse, parse_qs

class HTTPRequest:
    def __init__(self, path='/'):
        self.path = path
        self.parts = []
        self.params = None
        self.body = None

    def __str__(self) -> str:
        return "path: {}, parts{}, params: {}, body: {}".format(self.path, self.parts, self.params, self.body)
    
    def parse(self):
        parsed_url = urlparse(self.path)
        self.param = parse_qs(parsed_url.query)
        self.parts = self.path.split('/')[1:]