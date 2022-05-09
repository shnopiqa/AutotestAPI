# Ex12: Тест запроса на метод header
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
# Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
#
# =============================================================
# Результатом должна быть ссылка на коммит с тестом.

import requests


class TestHeadersCHeckFix:

    def test_headers_with_value(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response1.headers)

        headers_value = response1.headers.get('x-secret-homework-header')
        header = {'x-secret-homework-header': headers_value}

        assert header['x-secret-homework-header'] == 'Some secret value', f"Неверное значение {headers_value}"

