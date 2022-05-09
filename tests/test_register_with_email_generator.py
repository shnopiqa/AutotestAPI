import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions



class TestUserRegister(BaseCase):


    def test_creat_user_success(self):

        data = self.prepare_registration_data()

        respomse = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert respomse.status_code ==200, f"Unexpected status code {respomse.status_code}"

        Assertions.assert_code_status(respomse, 200)
        Assertions.assert_json_has_key(respomse, "id")



    def test_create_user_with_exciting_email(self):
        email = "vinkotov@example.com"

        data = self.prepare_registration_data(email)

        respomse = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        # assert respomse.status_code == 400, f"Unexpected status cod, {respomse.status_code}"
        Assertions.assert_code_status(respomse, 400)
        assert respomse.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected content {respomse.content}"
