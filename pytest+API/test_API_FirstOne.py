import requests


class TestFirstAPi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Vitaly"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dikt = response.json()

        assert "answer" in response_dikt, "There is no field 'answer' in response"

        expecter_response_text = f"Hello, {name}"

        actual_response_text = response_dikt["answer"]

        assert actual_response_text == expecter_response_text, "Actuall text in respinse is not correct"
