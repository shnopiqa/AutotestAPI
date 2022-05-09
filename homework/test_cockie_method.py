# Ex11: Тест запроса на метод cookie
#
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
# Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
#
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
import requests


class TestCookiesMethod:

    def test_homework_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_value = response.cookies.get('HomeWork')
        cookies = {'HomeWork': cookie_value}

        assert cookies['HomeWork'] == 'hw_value', f'Значение куки не верное {cookies}'
