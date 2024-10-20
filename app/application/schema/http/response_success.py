from dataclasses import dataclass
from http.client import HTTPResponse


@dataclass
class SuccessResponse(HTTPResponse):
    
    status_code: int = 200
