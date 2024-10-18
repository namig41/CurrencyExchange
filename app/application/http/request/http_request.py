from dataclasses import dataclass, field
import json
from typing import Any
from urllib.parse import unquote, urlparse, parse_qs

@dataclass
class HTTPRequest:
    
    path: str = field(default='/')
    parts: list[str] = field(default_factory=list)
    param: dict = field(default_factory=dict)
    body: Any = None
    
    def __str__(self) -> str:
        return "path: {}, parts{}, body: {}".format(self.path, self.parts, self.body)
    
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
