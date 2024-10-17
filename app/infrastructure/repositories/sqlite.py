from dataclasses import dataclass, field

from domain.entities.currency import Currency
from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.database.sqlite import SQLiteDatabase
from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document


@dataclass
class SQLLiteCurrenciesRepository(BaseCurrenciesRepository):
    
    sqlite_db_client: SQLiteDatabase
    currency_dao: CurrenciesDAO
    
    async def check_currency_exists_by_id(self, id: int) -> bool:
        currency: Currency = self.currency_dao.find_by_id(id)
        return currency is not None
        
    async def get_currency_by_id(self, id: int) -> Currency | None:
        currency_data: dict = self.currency_dao.find_by_id(id)
        return convert_currency_document_to_entity(currency_data)
     
    async def add_currency(self, currency: Currency) -> None:
        currecny_data: dict = convert_currency_entity_to_document(currency)
        self.currency_dao.insert(currecny_data)