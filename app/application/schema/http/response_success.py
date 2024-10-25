from dataclasses import dataclass, field

from application.schema.http.response import HTTPResponse

@dataclass
class SuccessResponse(HTTPResponse):
    status_code: int = 200
    data: dict
