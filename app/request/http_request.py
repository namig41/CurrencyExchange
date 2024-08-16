import json
from urllib.parse import unquote, urlparse, parse_qs

class HTTPRequest:
    def __init__(self, path='/'):
        self.path = path
        self.parts = []
        self.params = None
        self.body = None

    def __str__(self) -> str:
        return "path: {}, parts{}, params: {}, body: {}".format(self.path, self.parts, self.params, self.body)
    
    def parse(self, headers, rfile):
        parsed_url = urlparse(self.path)
        self.param = parse_qs(parsed_url.query)
        self.parts = self.path.split('/')[1:]
        index = self.parts[-1].find("?")
        self.parts[-1] = self.parts[-1] if index == -1 else self.parts[-1][:index]

        content_length = int(headers.get('Content-Length', 0))
        if content_length > 0:
            return 

        content = rfile.read(content_length).decode('utf-8')
        content_type = headers.get('Content-Type')
        if content_type == 'application/json':
            self.body = json.loads(content)
        elif content_type == 'application/x-www-form-urlencoded':
            self.body = parse_qs(content)
        else:
            self.body = content
