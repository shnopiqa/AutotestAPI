import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister:

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_creat_user_success(self):

        data = {
            "password": "123",
            "username": 'learnqa',
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email

        }

        respomse = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert respomse.status_code ==200, f"Unexpected status code {respomse.status_code}"

        Assertions.assert_code_status(respomse, 200)
        Assertions.assert_json_has_key(respomse, "id")



    def test_create_user_with_exciting_email(self):
        email = "vinkotov@example.com"

        data = {
            "password": "123",
            "username": 'learnqa',
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email

        }

        respomse = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert respomse.status_code == 400, f"Unexpected status cod, {respomse.status_code}"
        Assertions.assert_code_status(respomse, 400)
        assert respomse.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected content {respomse.content}"
