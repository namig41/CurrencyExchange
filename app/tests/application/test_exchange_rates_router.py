from http.server import HTTPServer

import requests


def test_get_exchange_rates(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchangeRates/")

    # Проверяем код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа
    expected_data = [
        {
            "id": 1,
            "baseCurrency": {
                "id": 1,
                "fullname": "United States dollar",
                "code": "USD",
                "sign": "$",
            },
            "targetCurrency": {
                "id": 2,
                "fullname": "Euro",
                "code": "EUR",
                "sign": "€",
            },
            "rate": 0.5,
        },
        {
            "id": 2,
            "baseCurrency": {
                "id": 1,
                "fullname": "United States dollar",
                "code": "USD",
                "sign": "$",
            },
            "targetCurrency": {
                "id": 3,
                "fullname": "Australian dollar",
                "code": "AUD",
                "sign": "A€",
            },
            "rate": 0.5,
        },
    ]

    assert response.json() == expected_data


def test_get_exchange_rates_required_field_missing(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchangeRates/AAA")

    # Проверяем код ответа
    assert response.status_code == 400

    # Проверяем содержимое ответа
    expected_data = {
        "message": "Exchange rate missing field",
    }

    assert response.json() == expected_data


def test_post_exchange_rates_add(http_server: HTTPServer):

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # Данные, которые отправим в POST-запросе
    payload = {
        "baseCurrencyCode": "EUR",
        "targetCurrencyCode": "AUD",
        "rate": 0.5,
    }

    # Отправляем GET-запрос к серверу
    response = requests.post(
        "http://localhost:8000/exchangeRates",
        data=payload,
        headers=headers,
    )

    # Проверяем код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа
    expected_data = {
        "id": 0,
        "baseCurrency": {
            "id": 2,
            "fullname": "Euro",
            "code": "EUR",
            "sign": "€",
        },
        "targetCurrency": {
            "id": 3,
            "fullname": "Australian dollar",
            "code": "AUD",
            "sign": "A€",
        },
        "rate": 0.5,
    }

    assert response.json() == expected_data
