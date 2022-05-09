
import requests
import pytest


class TestUserAgentApi:
    exclude_params = [

        ("User_agen1"),
        ("User_agen2")

    ]

    @pytest.mark.parametrize("condition", exclude_params)
    def test_user_agent_api(self, condition):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        user_agent = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"

        }

        response = requests.get(url, headers=user_agent)

        expected_values = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}

        if condition == "User_agen1":
            response_value = response.json()
            actual_values_platform = response_value["platform"]
            actual_values_browser = response_value["browser"]
            actual_values_device = response_value["device"]
            assert actual_values_device == expected_values["device"] and actual_values_browser == expected_values[
            "browser"] and actual_values_platform == expected_values["platform"], \
            f"Не совпадает {expected_values} и {actual_values_platform}, or {actual_values_browser} or {actual_values_device}"

        else:
            user_agent2 = {
            "User-Agent": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'}
            expected_values2 = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}

            response2 = requests.get(url, headers=user_agent2)
            response_value2 = response2.json()
            actual_values_platform = response_value2["platform"]
            print(actual_values_platform)
            actual_values_browser = response_value2["browser"]
            actual_values_device = response_value2["device"]
            print(actual_values_device)
            assert actual_values_device == expected_values2["device"] and actual_values_browser == expected_values2[
            "browser"] and actual_values_platform == expected_values2["platform"], \
            f"Не совпадает {expected_values2} и {actual_values_platform}, or {actual_values_browser} or {actual_values_device}"
