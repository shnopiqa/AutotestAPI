# Ex8: Токены
#
# Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ.
# Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам.
# В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще не готова,
# ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.
# Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job
#
# Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:
#
# * seconds - количество секунд, через сколько задача будет выполнена
# * token - тот самый токен, по которому можно получить результат выполнения нашей задачи
#
# Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:
#
# * error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
# * status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
# * result - будет только в случае, если задача готова, это поле будет содержать результат
#
# Наша задача - написать скрипт, который делал бы следующее:
#
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
#
# Как всегда, код нашей программы выкладываем ссылкой на комит.

import requests
import time
import json


class TokenCheckScrypt:

    def __init__(self):
        self.responeses = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
        self.response_text = self.responeses.text
        print(self.response_text)
        self.obj = json.loads(self.response_text)
        self.key = self.obj['token']

    def token_status_not_ready_check(self):
        responeses1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token': self.key})
        print(responeses1.text)
        status = json.loads(responeses1.text)
        key1 = status['status']
        if key1 == 'Job is NOT ready':
            print('status Is NoT Ready')
        else:
            raise TypeError(f'Wrong key: {key1}')

    def token_ready_status_check(self):
        time.sleep(self.obj['seconds'])
        self.responeses2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job',
                                        params={'token': self.key})
        self.status2 = json.loads(self.responeses2.text)
        self.key_status = self.status2['status']
        self.key_result = self.status2['result']
        if self.key_status == "Job is ready" or isinstance(self.key_result, int):
            print(f'все готово status: {self.key_status} result: {self.key_result}')
        else:
            raise TypeError(f'{self.key_status} {self.key_result}')


b = TokenCheckScrypt()
b.token_status_not_ready_check()
b.token_ready_status_check()
