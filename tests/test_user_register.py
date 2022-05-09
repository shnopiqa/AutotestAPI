import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister:


    def test_create_user_with_exciting_email(self):

        email = "vinkotov@example.com"

        data ={
            "password": "123",
            "username" : 'learnqa',
            "firstName" : "learnqa",
            "lastName" : "learnqa",
            "email" : email

        }

        respomse = requests.post("https://playground.learnqa.ru/api/user/", data =data)

        assert respomse.status_code == 400, f"Unexpected status cod, {respomse.status_code}"
        assert respomse.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected content {respomse.content}"



