import pytest
from task_6 import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("a", True),                # один символ
        ("aa", True),               # два одинаковых
        ("ab", False),              # два разных

        ("aba", True),              # нечётная длина
        ("abba", True),             # чётная длина

        ("abcba", True),
        ("abccba", True),

        ("abc", False),
        ("abca", False),

        ("", True),                 # пустая строка

        ("aaaaaa", True),           # все одинаковые
        ("abcdcba", True),
        ("abcdcbx", False),
    ],
    ids=[
        "single_char",
        "two_equal",
        "two_not_equal",

        "odd_length",
        "even_length",

        "odd_long",
        "even_long",

        "not_palindrome_short",
        "not_palindrome_close",

        "empty_string",

        "all_same",
        "long_palindrome",
        "long_not_palindrome",
    ],
)
def test_is_palindrome(s, expected):
    assert Solution.is_palindorm(s) == expected