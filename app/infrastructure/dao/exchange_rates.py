from dataclasses import dataclass, field
from infrastructure.dao.base import DAO

@dataclass
class CurrenciesDAO(DAO):
    table_name: str = field(default = "ExchangeRates")
    
