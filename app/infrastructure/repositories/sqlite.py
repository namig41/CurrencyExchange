from dataclasses import dataclass, field
from functools import lru_cache
from typing import Iterable

from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from infrastructure.database.base import BaseDatabase
from infrastructure.database.sqlite import SQLiteDatabase, sqlite_database_factory
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document, convert_exchange_rate_all_document_to_entity, convert_exchange_rate_document_to_entity, convert_exchange_rate_entity_to_document, convert_exchange_rates_document_to_entity


@dataclass
class SQLiteCurrenciesRepository(BaseCurrenciesRepository):
    
    currencies_dao: CurrenciesDAO
    
    def check_currency_exists_by_id(self, id: int) -> bool:
        currency: Currency = self.currencies_dao.find_by_id(id)
        return currency is not None
    
    def get_currencies(self) -> Iterable[Currency]:
        currenices: list[Currency] = [convert_currency_document_to_entity(currency_data)
                                      for currency_data in self.currencies_dao.find_all()]
        return currenices
        
        
    def get_currency_by_id(self, id: int) -> Currency | None:
        currency_data: dict = self.currencies_dao.find_by_id(id)
        
        if currency_data is None:
            return None
        
        return convert_currency_document_to_entity(currency_data)
    
    def get_currency_by_code(self, code: str) -> Currency | None:
        currency_data: dict = self.currencies_dao.find_by(code=code)
        
        if currency_data is None:
            return None
        
        return convert_currency_document_to_entity(currency_data)
     
    def add_currency(self, currency: Currency) -> None:
        currecny_data: dict = convert_currency_entity_to_document(currency)
        del currecny_data['id']
        
        self.currencies_dao.insert(currecny_data)
        
        
@dataclass
class SQLiteExchangeRatesRepository(BaseExchangeRatesRepository):
    
    exchange_rates_dao: ExchangeRatesDAO
    
    def check_exchange_rate_exists_by_id(
        self,
        base_currency: Currency,
        target_currency: Currency
        ) -> bool:

        return self.get_exchange_rate_by_id(base_currency, target_currency) is not None

    def get_exchange_rate_by_id(
        self,
        base_currency: Currency,
        target_currency: Currency
        ) -> ExchangeRate | None:
        
        exchange_rate_data: dict = self.exchange_rates_dao.find_by(BaseCurrencyId=base_currency.id,
                                                                      TargetCurrencyId=target_currency.id)
        
        if exchange_rate_data is None:
            return None
        
        return convert_exchange_rate_document_to_entity(exchange_rate_data, base_currency, target_currency)
    
    def get_exchange_rate_by_codes(self, base_code: str, target_code: str) -> ExchangeRate | None:
        exchange_rate_data: dict = self.exchange_rates_dao.find_by_codes(base_code, target_code)
        
        if exchange_rate_data is None:
            return None
                
        return convert_exchange_rate_all_document_to_entity(exchange_rate_data)
     
    def add_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        exchange_rate_data: dict = convert_exchange_rate_entity_to_document(exchange_rate)
        
        exchange_rate_data['baseCurrencyId'] = exchange_rate_data['baseCurrency']['id']
        exchange_rate_data['targetCurrencyId'] = exchange_rate_data['targetCurrency']['id']
        del exchange_rate_data['baseCurrency']
        del exchange_rate_data['targetCurrency']
                
        self.exchange_rates_dao.insert(exchange_rate_data)
        
    def get_exchange_rates(self) -> Iterable[ExchangeRate]:
        exchange_rates_data = self.exchange_rates_dao.find_all()
        return convert_exchange_rates_document_to_entity(exchange_rates_data)
    
    def update_exchange_rate(self, exchange_rate: ExchangeRate) -> None:
        
        self.exchange_rates_dao.update(
            {'rate': exchange_rate.rate.value},
            BaseCurrencyId=exchange_rate.base_currency.id,
            TargetCurrencyId=exchange_rate.target_currency.id
        )
        
@lru_cache        
def sqlite_currencies_repository_factory() -> SQLiteCurrenciesRepository:
    database: BaseDatabase = sqlite_database_factory()
    currencies_dao = CurrenciesDAO(database=database)
    currencies_repository = SQLiteCurrenciesRepository(currencies_dao)
    return currencies_repository
    
@lru_cache
def sqlite_exchange_rates_repository_factory() -> SQLiteExchangeRatesRepository:
    database: BaseDatabase = sqlite_database_factory()
    exchange_rates_dao = ExchangeRatesDAO(database=database)
    exchange_rates_repository = SQLiteExchangeRatesRepository(exchange_rates_dao)
    return exchange_rates_repository
    