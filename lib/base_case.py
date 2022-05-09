import json.decoder
from requests import Response
from datetime import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'Cannot find cookie with name {cookie_name} in the last responce'
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response:Response, name):
        try:
            response_as_dict = response.json()

        except json.decoder.JSONDecodeError:

            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email = None):

        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        return {
            "password": "123",
            "username": 'learnqa',
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }






