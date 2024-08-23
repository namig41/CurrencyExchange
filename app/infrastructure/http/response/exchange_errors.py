from app.infrastructure.http.response.common_error import NotFound

class ExchangeNotFoundError(NotFound):
    def __init__(self):
        super().__init__('Exchange not found')

