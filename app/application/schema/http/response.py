from dataclasses import dataclass


@dataclass
class HTTPResponse:
    
    status_code: int
    data: dict