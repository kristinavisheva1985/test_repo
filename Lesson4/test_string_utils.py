import pytest
from string_utils import StringUtils

string_utils = StringUtils()


def test_capitalize():
    assert string_utils.capitalize("кристина") == "Кристина"

def test_capitalize_negative():
    assert string_utils.capitalize("123") == "123"

def test_trim():
    assert string_utils.trim(" кристина") == "кристина"

def test_trim_negative():
    assert string_utils.trim("123") == "123"

> Mariia:
@pytest.mark.parametrize('string, symbol, result', [
    ("корень", "к", "орень"),
    ("Женя", "н", "Жея"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Красная Площадь", " ", "КраснаяПлощадь"),
])
def test_delete_symbol(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [

    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир  ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),
    ("Москва", "м", False),
    ("привет", "з", False),
    ("кот", "№", False)
])
def test_contains(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result
