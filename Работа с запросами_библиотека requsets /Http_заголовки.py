import requests

headers = {"some_header": "123"}

responses = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)

print(responses.text)
print(responses.headers)

