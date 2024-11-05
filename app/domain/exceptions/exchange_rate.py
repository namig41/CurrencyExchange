from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EqualCurrencyException(ApplicationException):
    @property
    def message(self):
        return "В обменнике валюты не должны совпадать"
