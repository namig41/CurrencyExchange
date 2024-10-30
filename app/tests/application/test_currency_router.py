from http.server import HTTPServer
import requests

def test_get_currency(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/currency/EUR")
    
    # Проверяем код ответа
    assert response.status_code == 200
    
    # Проверяем содержимое ответа
    expected_data = {
        "id": 2,
        "code": "EUR",
        "fullname": "Euro",
        "sign": "€"
    }  
    
    assert response.json() == expected_data
    
    
def test_get_currency_required_field_missing(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/currency/")
    
    # Проверяем код ответа
    assert response.status_code == 400
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Required field is missing"
    }  
    
    assert response.json() == expected_data
    
def test_get_currency_not_found(http_server: HTTPServer):
    # Отправляем GET-запрос к серверу
    response = requests.get("http://localhost:8000/currency/AAA")
    
    # Проверяем код ответа
    assert response.status_code == 404
    
    # Проверяем содержимое ответа
    expected_data = {
        "message": "Currency not found"
    }  
    
    assert response.json() == expected_data