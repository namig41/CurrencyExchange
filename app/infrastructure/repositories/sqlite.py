from dataclasses import dataclass, field
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from infrastructure.database.base import BaseDatabase
from infrastructure.database.sqlite import SQLiteDatabase, sqlite_database_factory
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document, convert_exchange_rate_document_to_entity, convert_exchange_rate_entity_to_document


@dataclass
class SQLiteCurrenciesRepository(BaseCurrenciesRepository):
    
    currencies_dao: CurrenciesDAO
    
    async def check_currency_exists_by_id(self, id: int) -> bool:
        currency: Currency = self.currencies_dao.find_by_id(id)
        return currency is not None
    
    async def get_currencies(self) -> Iterable[Currency]:
        currenices: list[Currency] = [convert_currency_document_to_entity(currency_data)
                                      for currency_data in self.currencies_dao.find_all()]
        return currenices
        
        
    async def get_currency_by_id(self, id: int) -> Currency | None:
        currency_data: dict = self.currencies_dao.find_by_id(id)
        
        if currency_data is None:
            return None
        
        return convert_currency_document_to_entity(currency_data)
     
    async def add_currency(self, currency: Currency) -> None:
        currecny_data: dict = convert_currency_entity_to_document(currency)
        self.currencies_dao.insert(currecny_data)
        
        
@dataclass
class SQLiteExchangeRatesRepository(BaseExchangeRatesRepository):
    
    exchange_rates_dao: ExchangeRatesDAO
    
    async def check_exchange_rate_exists_by_base_target_currency(
        self,
        base_currency: Currency,
        target_currency: Currency
        ) -> bool:
        exchange_rate_data: ExchangeRate = self.exchange_rates_dao.find_by(BaseCurrencyId=base_currency.id,
                                                                      TargetCurrencyId=target_currency.id)
        return exchange_rate_data is not None

    async def get_exchange_rate_by_id(
        self,
        base_currency: Currency,
        target_currency: Currency
        ) -> ExchangeRate | None:
        
        exchange_rate_data: ExchangeRate = self.exchange_rates_dao.find_by(BaseCurrencyId=base_currency.id,
                                                                      TargetCurrencyId=target_currency.id)
        
        if exchange_rate_data is None:
            return None
        
        return convert_exchange_rate_document_to_entity(exchange_rate_data, base_currency, target_currency)
     
    async def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        exchange_rate_data: dict = convert_exchange_rate_entity_to_document(exchange_rate)
        self.exchange_rates_dao.insert(exchange_rate_data)
        
def sqlite_currencies_repository_factory() -> SQLiteCurrenciesRepository:
    database: BaseDatabase = sqlite_database_factory()
    currencies_dao = CurrenciesDAO(database=database)
    currencies_repository = SQLiteCurrenciesRepository(currencies_dao)
    return currencies_repository
    
def sqlite_exchange_rates_repository_factory() -> SQLiteExchangeRatesRepository:
    database: BaseDatabase = sqlite_database_factory()
    exchange_rates_dao = ExchangeRatesDAO(database=database)
    exchange_rates_repository = SQLiteExchangeRatesRepository(exchange_rates_dao)
    return exchange_rates_repository
    