from dataclasses import dataclass

from domain.exceptions.currency_code import CodeIsIvalideException
from domain.value_objects.base import BaseValue


@dataclass(frozen=True)
class Code(BaseValue[str]):
    value: str

    def validate(self):
        if len(self.value) != 3:
            raise CodeIsIvalideException()

    def as_generic_type(self) -> str:
        return self.value
