import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data = {"param1":"value1"})
print(response.text)

"""ЕСЛИ У ЗАПРОСА МЕТОД GET, 
ТО ИСПОЛЬЗУЕТСЯ ПЕРЕМЕННАЯ params,  
ЕСЛИ У ЗАПРОСА МЕТОДА PUT, POST, DELETE, 
ТО НУЖНО ИСПОЛЬЗОВАТЬ ПЕРЕМЕННУЮ data """

