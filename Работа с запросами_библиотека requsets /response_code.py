"""
КОДЫ ОТВЕТА ОТ СЕРВЕРА
100 - 199 - информационные
200 - 299 Успех
300 - 399 Перенаправление
400 499 ОШибка клиента
500 599 ОШибка сервера

САМЫЕ ПОПУЛЯРНЫЕ КОДЫ:

200 - УСПЕШНЫЙ ЗАПРОС
301 ПЕРЕНАПРАВЛЕНИЕ НА ДРУГОЙ URL:
403 РЕСУРС ЗАПРЕЩЕН ДЛЯ КЛИЕНТА
404 ЗАПРОС НА ПУСТОЙ URL :
500 СЕРВЕР НЕ ОБРАБОТАЛ ЗАПРОС
"""
import requests

responses = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# сначала наткнулс на редирект и перестал переходит при False
# если allow_redirects == True то метод будет ждать пока не произойдет редирект на сайт
first_response = responses.history[0]
second_response = responses

print(first_response.url)
print(second_response.url)
print(responses.status_code)
print(responses.text)

