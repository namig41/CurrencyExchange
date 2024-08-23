class HTTPResponse:
    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code
        self.data = data
