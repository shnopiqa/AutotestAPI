import requests
import json
string_as_json_format = '{"answer": "Hello, User"}'

obj = json.loads(string_as_json_format)


key = 'answer'

if key in obj:
    print(obj[key])
else:
    raise TypeError(f"Ключа {key} нет")



