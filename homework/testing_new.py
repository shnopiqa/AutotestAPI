
import requests
import json

# data = {
#             "email": "vinkotov@example.com",
#             "password": "1234"
#         }
#
# response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
#
# print(response1.cookies)
#
# # auth_sid = self.get_cookie(response1, "auth_sid")
# #
# # token = self.get_headers(response1, "x-csrf-token")

data = {
    "email": "vinkotov@example.com",
    "password": "1234"
}
response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

print(response1.cookies)
print(response1.headers)

user_id_from_aut_method = response1.json()
print(user_id_from_aut_method)
token = "d02f0e2b406004abd2c6a6ce5661c241dbc0a0d902e94918f1549272bcf2cafc2634fd9d"
auth_sid = "7ea3427b90f02cfb3bbdb2e62d28f23002e94918f1549272bcf2cafc2634fd9d"

respomse2 = requests.get (
    "https://playground.learnqa.ru/api/user/2",
    headers={"x-csrf-token": token},
    cookies={"auth_sid": auth_sid}
)
print(respomse2.text)