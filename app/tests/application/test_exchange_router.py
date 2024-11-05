from http.server import HTTPServer

import requests


def test_get_exchange(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchange?from=USD&to=AUD&amount=10")

    # Проверяем код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа
    expected_data = {
        "id": 2,
        "baseCurrency": {
            "id": 1,
            "code": "USD",
            "fullname": "United States dollar",
            "sign": "$",
        },
        "targetCurrency": {
            "id": 3,
            "code": "AUD",
            "fullname": "Australian dollar",
            "sign": "A€",
        },
        "rate": 0.5,
        "amount": 10.0,
        "convertedAmount": 5.0,
    }

    assert response.json() == expected_data


def test_get_reverse_exchange(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchange?from=AUD&to=USD&amount=10")

    # Проверяем код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа
    expected_data = {
        "id": 2,
        "baseCurrency": {
            "id": 1,
            "code": "USD",
            "fullname": "United States dollar",
            "sign": "$",
        },
        "targetCurrency": {
            "id": 3,
            "code": "AUD",
            "fullname": "Australian dollar",
            "sign": "A€",
        },
        "rate": 0.5,
        "amount": 10.0,
        "convertedAmount": 20.0,
    }

    assert response.json() == expected_data
