"""
COOKIE - ЭТО СПЕЦИАЛЬНЫЕ ФАЙЛЫ ИХ СОЗДАЕТ КЛИЕНТ, МОБИЛЬНОЕ ПРИЛОЖЕНИ ИЛИ БРАУЗЕР
НА ОСНОВЕ ОТВЕТА СЕРВЕРА
ЭТИ ФАЙЛЫ ИМЕЮТ СРОК ГОДНОСТИ ПОСЛЕ КОТОРОГО ОНИ УДАЛЯЮТСЯ КЛИЕНТОМ
 У КУКИ ЕСТЬ ИМЯ, ЗНАЧЕНИЕ И ПРИНАДЛЕЖНОСТЬ К КАКОМУ-ТО ДОМЕНУ, КАЖДЫЙ РАЗ КОНГДА КЛИЕНТ СОЗДАЕТ HTTP ЗАПРОС К СЕРВЕРУ ОН ПРИКЛАДЫВАЕТ ВСЕ КУКИ К СЕРВЕРУ, КОТОРЫЕ
  КАСАЮТСЯ ДОМЕНА К КОТОРОМУ ЗАПРОС ДЕЛАЕТСЯ
  САМЫЙ ПОПУЛЯРНЫЙ СПОСОБ ИСПОЛЬЗОВАНИЯ КУКИ - АВТОРИЗАЦИЯ
  КОГДА КЛИЕНТ ПРИХОДИТ НА СЕРВЕР НЕ БУДУЧИ АВТОРИЗОВАННЫМ, САЙТ ПРОСИТ ЕГО ВВЕСТИ ЛОГИН И ПАРОЛЬ, ЭТИ ДАННЫЕ С HTTP ЗАПРОСМ УХОДЯТ НА СЕРВЕР, СЕРВЕР ПРОВЕРЯТ, ЕСЛИ КОРРЕКТНЫ
  СЕРВЕР ПРИСЫЛАЕТ КУКИ С ИМЕНЕМ И ЗНАЧЕНИЕМ КОТОРЫЕ БУДУТ ТОЛЬКО У ЭТОГО ПОЛЬЗОВАТЕЛЯ
  В СЛЕУДУЮЩИЙ РАЗ СЕРВЕР СМОЖЕТ УЗНАТЬ ПОЛЬЗОВАТЕЛЯ ПО КУКАМ
  ТАК ЖЕ СЕРВЕР БЛАГОДАРЯ КУКИ СЕРВЕР МОЖЕТ ОТСЛЕЖИВАТЬ ДЕЙСТВИЯ НА САЙТЕ
  """
import requests

payload = {"login" : "secret_login", "password" : "secret_pass"}

response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get("auth_cookie")

cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie" : cookie_value})


response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)

