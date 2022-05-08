"""
ЧЕМ ТЕСТЫ ОТЛИЧАЮТСЯ ОТ КОДА, НАПИСАННОГО НА ПАЙТОН?
ТЕСТ ТАКОЙ ЖЕ КОД КОТОРЫЙ ОПИСЫВАЕТ ПОСЛЕДОВАТЕЛЬНОСТЬ ДЕЙСТВИЙ
НО В ТЕСТАХ ДОЛЖНЫ БЫТЬ ПРОВЕРКИ СРАВНЕНИЯ ОЖИДАЕМОГО РЕЗУЛЬТАТА
С ДЕЙСТВИТЕЛЬНЫМ РЕЗУЛЬТАТОМ
"""


class TestExample:
    def test_check_math(self):
        d = 5
        b = 9
        expected_some = 14
        assert d + b == expected_some, f"Some of variables are {d} plus {b} not equal {expected_some}"

    def test_check_math2(self):
        d = 5
        b = 3
        expected_some = 14
        assert d + b == expected_some, f"Some of variables are {d} plus {b} not equal {expected_some}"



