import json


class PythonCHek:
    def __init__(self):
        self.json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
        self.obj = json.loads(self.json_text)
        self.key = self.obj['messages']

    def check(self):
        if self.key[1]['message'] == 'And this is a second message':
            print(self.key[1]['message'])
        else:
            raise TypeError('Error')


b = PythonCHek()

