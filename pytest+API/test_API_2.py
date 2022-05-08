import pytest
import requests


class TestFirstAPi:
    names = [
        ("Vitalii"),
        ("Arsenii"),
         ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dikt = response.json()

        assert "answer" in response_dikt, "There is no field 'answer' in response"

        expecter_response_text = f"Hello, {name}"

        actual_response_text = response_dikt["answer"]

        assert actual_response_text == expecter_response_text, f"Actuall text in respinse is not correct  excepted {actual_response_text} actual respose is {expecter_response_text}"
