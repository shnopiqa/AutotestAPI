import requests
import simplejson


response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)


except simplejson.JSONDecodeError:
    print("Response as not JSON Format")

