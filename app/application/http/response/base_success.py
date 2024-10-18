from infrastructure.http.response.http_response import HTTPResponse

class SuccessResponse(HTTPResponse):
    def __init__(self, data: dict):
        super().__init__(200, data)