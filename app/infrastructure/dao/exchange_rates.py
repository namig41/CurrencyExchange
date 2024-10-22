from dataclasses import dataclass, field
from typing import Any
from infrastructure.dao.base import DAO

@dataclass
class ExchangeRatesDAO(DAO):
    table_name: str = field(default = "ExchangeRates", kw_only=True)
            
    def find_all(self) -> list[dict[Any, Any]]:
        query = """SELECT 
                exchangerates.id,
                Rate,
                tc.Id AS TargetID, 
                tc.Code AS TargetCode, 
                tc.FullName AS TargetFullName,
                tc.Sign AS TargetSign, 
                bc.Id AS BaseID, 
                bc.Code AS BaseCode, 
                bc.FullName AS BaseFullName, 
                bc.Sign AS BaseSign
                FROM exchangerates
                INNER join currencies tc on exchangerates.basecurrencyid = tc.id 
                INNER join currencies bc on exchangerates.targetcurrencyid = bc.id"""
        
        result = self.database.execute(query)

        columns = [desc[0].lower() for desc in result.description]
        rows = result.fetchall()

        results = [dict(zip(columns, row)) for row in rows]
        return results