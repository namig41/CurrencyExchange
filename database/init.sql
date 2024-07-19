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
    BaseCurrencyId INTEGER,
    TargetCurrencyId INTEGER,
    Rate DECIMAL(6, 2),
    FOREIGN KEY (BaseCurrencyId) REFERENCES Currencies(ID),
    FOREIGN KEY (TargetCurrencyId) REFERENCES Currencies(ID),
    UNIQUE (BaseCurrencyId, TargetCurrencyId)
);

INSERT INTO Currencies (ID, Code, FullName, Sign) 
VALUES 
    (1, 'USD', 'United States dollar', '$'),
    (2, 'EUR', 'Euro', '€'),
    (3, 'AUD', 'Australian dollar', 'A€');

INSERT INTO ExchangeRates (ID, BaseCurrencyId, TargetCurrencyId, Rate) 
VALUES 
    (1, 1, 2, 0.92),
    (2, 1, 3, 1.45);