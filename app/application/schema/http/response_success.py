from dataclasses import dataclass

from application.schema.http.response import HTTPResponse

@dataclass
class SuccessResponse(HTTPResponse):
    
    status_code: int = 200
