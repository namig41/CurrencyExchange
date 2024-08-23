from dataclasses import dataclass

@dataclass
class Currency:
    id: int
    code: str
    fullname: str
    sign: str

