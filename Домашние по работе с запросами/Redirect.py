import requests

responses = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
# сначала наткнулс на редирект и перестал переходит при False
# если allow_redirects == True то метод будет ждать пока не произойдет редирект на сайт
first_response = responses.history[0]
print(first_response.url)
print(responses.history)
second_response = responses.history[1]
print(second_response)
print(responses.url)
