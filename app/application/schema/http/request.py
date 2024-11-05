from dataclasses import (
    dataclass,
    field,
)
from typing import Any


@dataclass
class HTTPRequest:

    path: str = field(default="/")
    parts: list[str] = field(default_factory=list)
    param: dict = field(default_factory=dict)
    body: Any = None
