from dataclasses import dataclass, field


@dataclass
class HTTPResponse:
    data: dict = field(default=dict, kw_only=True)
    status_code: int
