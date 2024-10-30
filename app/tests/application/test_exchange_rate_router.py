from http.server import HTTPServer
import requests

def test_get_exchange_rate(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchangeRate/USDAUD")
    
    # Проверяем код ответа
    assert response.status_code == 200
    
    # Проверяем содержимое ответа
    expected_data = {
        "id": 2,
        "baseCurrency": {
            "id": 1,
            "fullname": "United States dollar",
            "code": "USD",
            "sign": "$"
        },
        "targetCurrency": {
            "id": 3,
            "fullname": "Australian dollar",
            "code": "AUD",
            "sign": "A€"
        },
        "rate": 1.45
    } 
    
    assert response.json() == expected_data
    
    
def test_get_exchange_rate_required_field_missing(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchangeRate/")
    
    # Проверяем код ответа
    assert response.status_code == 400
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Exchange rate missing field"
    }  
    
    assert response.json() == expected_data
    
def test_get_exchange_rate_not_found(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/exchangeRate/USDAAA")
    
    # Проверяем код ответа
    assert response.status_code == 404
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Exchange rate for pair not found"
    }  
    
    assert response.json() == expected_data