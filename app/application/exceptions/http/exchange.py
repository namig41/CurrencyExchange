from dataclasses import dataclass
from application.exceptions.http.common import BadRequestException, NotFoundException, RequiredFieldException

@dataclass(eq=False)
class ExchangeNotFoundException(NotFoundException):

    @property
    def message(self):
        return 'Валюта не найдена'
    