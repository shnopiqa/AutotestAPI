import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")

    ]

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        self.response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        self.auth_sid = self.get_cookie(self.response1, "auth_sid")
        self.token = self.get_headers(self.response1, "x-csrf-token")
        self.user_id_from_aut_method = self.get_json_value(self.response1, "user_id")

        # assert "user_id" in self.response1.json(), "THere is no user id in the response"
        # self.user_id_from_aut_method = self.response1.json()["user_id"]

    def test_auth_user(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            'user_id',
            self.user_id_from_aut_method,
            "User is from auth method is not equal to user if from chek method"
        )

        # assert "user_id" in response2.json(), "There is no user if in the second response"
        # user_id_from_check_method = response2.json()["user_id"]
        # assert self.user_id_from_aut_method == user_id_from_check_method, "User if from AuthMethod is not equal to user id from check method"

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={'x-csrf-token': self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={'auth_sid': self.auth_sid}
            )

            Assertions.assert_json_value_by_name(
                response2,
                "user_id",
                0,
                f"User is authorized with collection {condition}"
            )

        # assert "user_id" in self.response1.json(), "There is no user id in the second response"
        #
        # user_id_from_check_method = response2.json()["user_id"]
        #
        # assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"