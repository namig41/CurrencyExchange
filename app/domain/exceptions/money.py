from dataclasses import dataclass
from domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class MoneyInvalidValueException(ApplicationException):
    @property
    def message(self):
        return 'Значение денег не может быть отрицательным'