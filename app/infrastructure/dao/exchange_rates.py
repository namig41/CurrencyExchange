from dataclasses import (
    dataclass,
    field,
)

from infrastructure.dao.base import DAO


@dataclass
class ExchangeRatesDAO(DAO):
    table_name: str = field(default="ExchangeRates", kw_only=True)

    def find_all(self) -> list[dict]:
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
                INNER join currencies bc on exchangerates.basecurrencyid = bc.id
                INNER join currencies tc on exchangerates.targetcurrencyid = tc.id"""

        result = self.database.execute(query)

        columns = [desc[0].lower() for desc in result.description]
        rows = result.fetchall()

        results = [dict(zip(columns, row)) for row in rows]
        return results

    def find_by_codes(self, base_code: str, target_code: str) -> dict:
        query = f"""SELECT
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
                INNER join currencies bc on exchangerates.basecurrencyid = bc.id
                INNER join currencies tc on exchangerates.targetcurrencyid = tc.id
                WHERE bc.Code = '{base_code}' AND tc.Code = '{target_code}'"""

        result = self.database.execute(query)

        if result:
            columns = [desc[0].lower() for desc in result.description]
            data = result.fetchone()
            if not data:
                return None
            return dict(zip(columns, data))

        return None
