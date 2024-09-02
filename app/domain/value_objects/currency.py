from dataclasses import dataclass

@dataclass(frozen=True)
class Currency:
    id: int
    code: str
    fullname: str
    sign: str

