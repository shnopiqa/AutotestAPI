# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
#
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого
# вы делаете запрос. Например, если вы делаете GET-запрос, параметр method должен равняться строке
# ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’. И так далее.

# Надо написать скрипт, который делает следующее:
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
#
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=
#
# Итогом должна быть ссылка на коммит со скриптом и ответы на все 4 вопроса.


import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)        # WRONG MEHOD PROVIDED
print(response.status_code)
print(response.url)

#BAD REQUESTS
params = {"method" : "HEAD"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = params)
print(params)
print(response.text)
print(response.status_code)

params = {"method" : "HEAD"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data= params)
print(params)
print(response.text)        # WRONG MEHOD PROVIDED
print(response.status_code)

params = {"method" : "HEAD"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data= params)
print(params)
print(response.text)        # WRONG MEHOD PROVIDED
print(response.status_code)

params = {"method" : "HEAD"}
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data= params)
print(params)
print(response.text)        # WRONG MEHOD PROVIDED
print(response.status_code)


#GOOD REQUEST
params = {"method" : "GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = params)
print(params)
print(response.text)        # {"success":"!"}
print(response.status_code)

params = {"method" : "PUT"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data= params)
print(params)
print(response.text)        # {"success":"!"}
print(response.status_code)

params = {"method" : "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data= {"method" : "POST"})
print(response.text)        # {"success":"!"}
print(response.status_code)

response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data= {"method" : "DELETE"})
print(response.text)        # {"success":"!"}
print(response.status_code)

#  CYCLE_CHEK

RESP = {"GET", "PUT", "POST", "DELETE"}

for i in RESP:
    params = {"method" : i}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=params)
    print(params)
    print(response.text)
    print(response.status_code)

for i in RESP:
    params = {"method": i}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    print(params)
    print(response.text)
    print(response.status_code)

for i in RESP:
        params = {"method": i}
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
        print(params)
        print(response.text)
        print(response.status_code)

for i in RESP:
        params = {"method": i}
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
        print(params)
        print(response.text)
        print(response.status_code)