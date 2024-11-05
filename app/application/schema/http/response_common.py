from dataclasses import (
    dataclass,
    field,
)

from application.schema.http.response import HTTPResponse


@dataclass
class SuccessResponse(HTTPResponse):
    status_code: int = 200
    data: dict


@dataclass
class NotFoundResponse(HTTPResponse):
    status_code: int = 404
    data: dict = field(default_factory=lambda: {"message": "Not Found"})
