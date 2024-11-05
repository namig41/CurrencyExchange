from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class RateIsNegativeException(ApplicationException):
    @property
    def message(self):
        return "Обменный курс не может быть отрицательной"
