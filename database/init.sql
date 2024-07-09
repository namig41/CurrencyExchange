DROP TABLE IF EXISTS Currencies;
DROP TABLE IF EXISTS ExchangeRates;

CREATE TABLE IF NOT EXISTS Currencies (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code TEXT UNIQUE,
    FullName TEXT,
    Sign TEXT
);

CREATE TABLE IF NOT EXISTS ExchangeRates (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BaseCurrencyId INTEGER UNIQUE,
    TargetCurrencyId INTEGER UNIQUE,
    Rate DECIMAL(6, 2)
);

INSERT INTO Currencies (Code, FullName, Sign) 
VALUES 
    ('USD', 'United States dollar', '$'),
    ('EUR', 'Euro', '€');