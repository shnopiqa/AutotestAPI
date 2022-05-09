import pytest
#
#
# class TestShortPhraseTest:
#
#     def test_input_short_phrase(self):
#         phrase = input("Set a phrase: ")
#         assert len(phrase) < 15, f"Frase is biiger then 15 symbols"

import requests



class TestUserAgentApi:

    def test_user_agent_api(self):
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


