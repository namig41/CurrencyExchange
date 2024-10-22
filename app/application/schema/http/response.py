from dataclasses import dataclass, field


@dataclass
class HTTPResponse:
    
    status_code: int
    data: dict = field(default=dict)