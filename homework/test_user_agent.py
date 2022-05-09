# Ex13: User Agent
#
# User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос.
# Он формируется автоматически клиентом, например браузером.
# Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
#
# Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
# Метод определяет по строке заголовка User Agent следующие параметры:
#
# device - iOS или Android
#
# browser - Chrome, Firefox или другой браузер
#
# platform - мобильное приложение или веб
#
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
#
# Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.
#
# Список User Agent и ожидаемых значений можно найти по этой ссылке: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26
#
# Пример того, как должен выглядеть запрос с указанным User Agent:
#
# requests.get(
#
#     "https://playground.learnqa.ru/ajax/api/user_agent_check",
#
#     headers={"User-Agent": "Some value here"}
#
# )
#
# ============================================================
# На самом деле метод не всегда работает правильно. Ответом к задаче должен быть список из тех User Agent,
# которые вернули неправильным хотя бы один параметр, с указанием того, какой именно параметр неправильный.
# И, конечно, ссылка на коммит с вашим тестом.


import requests
import pytest


class TestUserAgentApi:
    exclude_params = [
        ("User_agen1"),
        ("User_agent2"),
        ("User_agent3")

    ]

    @pytest.mark.parametrize("condition", exclude_params)
    def test_user_agent_api(self, condition):
        user_agent1 = [
            {
                "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
            },

            {
                "User-Agent": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'
            },

            {
                "User-Agent": 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
             }
        ]

        expected_values = [

            {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
            {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
            {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}

            ]

        if condition == "User_agen1":
            response_test = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=user_agent1[0])
            response_value = response_test.json()
            actual_values_platform = response_value["platform"]
            actual_values_browser = response_value["browser"]
            actual_values_device = response_value["device"]
            assert actual_values_device == expected_values[0]["device"] and actual_values_browser == expected_values[0][
                "browser"] and actual_values_platform == expected_values[0]["platform"], \
                f"Не совпадает {expected_values} и {actual_values_platform}, or {actual_values_browser} or {actual_values_device}"

        elif condition == "User_agen2":
            response_test = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=user_agent1[1])
            response_value = response_test.json()
            actual_values_platform = response_value["platform"]
            actual_values_browser = response_value["browser"]
            actual_values_device = response_value["device"]

            assert actual_values_device == expected_values[1]["device"] and actual_values_browser == expected_values[1][
                "browser"] and actual_values_platform == expected_values[1]["platform"], \
                f"Не совпадает {expected_values} и [{actual_values_platform}, {actual_values_browser}, {actual_values_device}]"
        elif condition == "User_agen3":
            response_test = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                         headers=user_agent1[2])
            response_value = response_test.json()
            actual_values_platform = response_value["platform"]
            print(actual_values_platform)
            actual_values_browser = response_value["browser"]
            actual_values_device = response_value["device"]


            assert actual_values_device == expected_values[2]["device"] and actual_values_browser == expected_values[2][
                "browser"] and actual_values_platform == expected_values[2]["platform"], \
                f"Не совпадает {expected_values} и [{actual_values_platform}, {actual_values_browser}, {actual_values_device}]"
