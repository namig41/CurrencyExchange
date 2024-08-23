from app.infrastructure.http.response.http_response import HTTPResponse

class ErrorResponse(HTTPResponse):
    def __init__(self, status_code: int, message: str):
        super().__init__(status_code, {'error': message})

