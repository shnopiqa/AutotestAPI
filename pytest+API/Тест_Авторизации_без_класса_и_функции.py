import requests


data = {
    "email": "vinkotov@example.com",
     "password": "1234"
}

response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
# print(response1.text)
# print(response1.cookies)
# print(response1.headers)
# print(response1.json())

assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
assert "x-csrf-token" in response1.headers, "There is not CSRF token header in the response"
assert "user_id" in response1.json(), "THere is no user id in the response"

auth_sid = response1.cookies.get("auth_sid")
print(auth_sid)
token = response1.headers.get("x-csrf-token")
print(token)
user_id_from_aut_method = response1.json()["user_id"]
print(user_id_from_aut_method)

response2 = requests.get(
"https://playground.learnqa.ru/api/user/auth",
headers={"x-csrf-token": token},
cookies={"auth_sid": auth_sid})

print(response2.text)
print(response2.cookies)
print(response2.headers)
print(response2.json())


assert "user_id" in response2.json(), "There is no user if in the second response"

user_id_from_check_method = response2.json()["user_id"]
print(user_id_from_check_method)

assert user_id_from_aut_method == user_id_from_check_method, "User if from AuthMethod is not equal to user id from check method"
