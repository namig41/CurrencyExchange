from response.base_error import ErrorResponse

class BadRequest(ErrorResponse):
    def __init__(self, message: str = "Bad request"):
        super().__init__(400, message)

class NotFound(ErrorResponse):
    def __init__(self, message: str = "Not Found"):
        super().__init__(404, message)

class Conflict(ErrorResponse):
    def __init__(self, message: str):
        super().__init__(409, message)

class InternalServerError(ErrorResponse):
    def __init__(self, message: str = "Internel Sever Error"):
        super().__init__(500, message)

class RequiredFieldMissingError(BadRequest):
    def __init__(self):
        super().__init__('Required field is missing')

class DatabaseError(InternalServerError):
    def __init__(self):
        super().__init__('Database not exist')