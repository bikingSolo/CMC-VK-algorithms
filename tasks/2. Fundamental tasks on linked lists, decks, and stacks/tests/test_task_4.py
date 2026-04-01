import pytest
from task_4 import Solution


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("abc", "abc", True),            # одинаковые строки
        ("abc", "aXbYc", True),          # вставки между символами
        ("abc", "abxc", True),           # вставка в середине
        ("abc", "xabc", True),           # вставка в начале
        ("abc", "abcx", True),           # вставка в конце
        ("", "abc", True),               # пустая строка — всегда подпоследовательность
        ("abc", "ac", False),            # удаление символа
        ("abc", "ab", False),            # укороченная строка
        ("abc", "def", False),           # нет совпадений
        ("abc", "cab", False),           # порядок нарушен
    ],
    ids=[
        "equal",
        "interleaved_insertions",
        "middle_insertion",
        "prefix_insertion",
        "suffix_insertion",
        "empty_str1",
        "missing_char",
        "shorter_str2",
        "no_match",
        "wrong_order",
    ],
)
def test_compare_strings(str1, str2, expected):
    assert Solution.compare_strings(str1, str2) == expected