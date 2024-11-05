from dataclasses import dataclass

from application.exceptions.http.common import NotFoundException


@dataclass(eq=False)
class ExchangeNotFoundException(NotFoundException):

    @property
    def message(self):
        return "Валюта не найдена"
