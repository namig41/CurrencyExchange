from http.server import HTTPServer
import requests

def test_get_currencies(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/currencies")
    
    # Проверяем код ответа
    assert response.status_code == 200
    
    # Проверяем содержимое ответа
    expected_data = [
        {
            "id": 1,
            "code": "USD",
            "fullname": "United States dollar",
            "sign": "$"
        },
        {
            "id": 2,
            "code": "EUR",
            "fullname": "Euro",
            "sign": "€"
        },
        {
            "id": 3,
            "code": "AUD",
            "fullname": "Australian dollar",
            "sign": "A€"
        }
    ]
    
    assert response.json() == expected_data
    
    
def test_get_currencies_required_field_missing(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/currencies/fd")
    
    # Проверяем код ответа
    assert response.status_code == 400
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Required field is missing"
    }  
    
    assert response.json() == expected_data
    
def test_post_currencies_add_new(http_server: HTTPServer):
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Данные, которые отправим в POST-запросе
    payload = {
        "name": "Russian Ruble",
        "code": "RUB",
        "sign": "₽"
    }
    
    # Отправляем POST-запрос к серверу
    response = requests.post("http://localhost:8000/currencies", data=payload, headers=headers)
    
    # Проверяем код ответа
    assert response.status_code == 200 
    
    # Проверяем содержимое ответа
    expected_data = {
        "id": 4,
        "fullname": "Russian Ruble",
        "code": "RUB",
        "sign": "₽"
    }
    
    assert response.json() == expected_data
    
def test_post_currencies_required_field_missing_with_empty_data(http_server: HTTPServer):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Отправляем POST-запрос к серверу
    response = requests.post("http://localhost:8000/currencies", headers=headers)
    
    # Проверяем код ответа
    assert response.status_code == 400
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Required field is missing"
    }  
    
    assert response.json() == expected_data
    
def test_post_currencies_required_field_missing(http_server: HTTPServer):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Данные, которые отправим в POST-запросе
    payload = {
        "name": "Russian Ruble",
        "sign": "₽"
    }
    
    # Отправляем POST-запрос к серверу
    response = requests.post("http://localhost:8000/currencies", data=payload, headers=headers)
    
    # Проверяем код ответа
    assert response.status_code == 400
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Required field is missing"
    }  
    
    assert response.json() == expected_data
    
def test_post_currencies_currency_exsists(http_server: HTTPServer):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Данные, которые отправим в POST-запросе
    payload = {
        "code": "USD",
        "name": "United States dollar",
        "sign": "$"
    }
    
    # Отправляем POST-запрос к серверу
    response = requests.post("http://localhost:8000/currencies", data=payload, headers=headers)
    
    # Проверяем код ответа
    assert response.status_code == 409
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Currency with code already exists"
    }  
    
    assert response.json() == expected_data