class HTTPRequest:
    def __init__(self, path, params, body):
        self.path = path
        self.params = params
        self.body = body