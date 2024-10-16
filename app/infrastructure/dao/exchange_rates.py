from dataclasses import dataclass, field
from infrastructure.dao.base import DAO

@dataclass
class ExchangeRatesDAO(DAO):
    table_name: str = field(default = "ExchangeRates", kw_only=True)
    
