import json
from abc import abstractmethod
from typing import Protocol
from urllib.parse import (
    parse_qs,
    urlparse,
)

from application.schema.http.request import HTTPRequest


class ParseHTTPRequestStrategy(Protocol):

    @abstractmethod
    def parse(self, path, headers, rfile) -> HTTPRequest: ...


class ParseRequest(ParseHTTPRequestStrategy):

    def parse(self, path, headers, rfile) -> HTTPRequest:
        http_request = HTTPRequest(path)

        # Parse URL and extract parameters and path parts
        parsed_url = urlparse(http_request.path)
        http_request.param = parse_qs(parsed_url.query)
        http_request.parts = [part for part in parsed_url.path.split("/") if part]

        # Determine content length and read content
        content_length = int(headers.get("Content-Length", 0))
        content = rfile.read(content_length).decode("utf-8")

        # Parse body based on Content-Type
        content_type = headers.get("Content-Type", "")
        if content_type == "application/json":
            try:
                http_request.body = json.loads(content)
            except json.JSONDecodeError:
                http_request.body = None  # or handle errors
        elif content_type == "application/x-www-form-urlencoded":
            http_request.body = parse_qs(content)
        else:
            http_request.body = content

        return http_request
