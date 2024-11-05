from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class CodeIsIvalideException(ApplicationException):
    @property
    def message(self):
        return "Неправильное значение кода валюты"
