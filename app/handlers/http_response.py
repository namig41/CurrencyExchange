class HTTPResponse:
    def __init__(self, status_code=200, data=None):
        self.status_code = status_code
        self.data = data
