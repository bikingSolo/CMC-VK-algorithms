import importlib.util
from pathlib import Path

import pytest


TASK_PATH = Path(__file__).resolve().parents[1] / "task_4.py"
SPEC = importlib.util.spec_from_file_location("task_4_module", TASK_PATH)
TASK_MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(TASK_MODULE)
Solution = TASK_MODULE.Solution


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("", "a", "a"),
        ("a", "ab", "b"),
        ("ab", "abc", "c"),
        ("abc", "cabd", "d"),
        ("abcd", "abcde", "e"),
        ("aabb", "abacb", "c"),
        ("zzz", "zzzz", "z"),
        ("xy", "yxz", "z"),
        ("hello", "hlelxo", "x"),
        ("kitten", "knitteq", "q"),
        ("1122", "12123", "3"),
        ("qwerty", "wqeyrtu", "u"),
    ],
    ids=[
        "empty_source",
        "single_letter",
        "simple_append",
        "shuffled_with_new_letter",
        "new_letter_at_end",
        "duplicates",
        "same_letter_added",
        "permuted_input",
        "word_case",
        "another_shuffle",
        "digit_character",
        "mixed_order",
    ],
)
def test_find_excess_letter(a, b, expected):
    assert Solution().find_excess_letter(a, b) == expected


def test_find_excess_letter_returns_single_character():
    result = Solution().find_excess_letter("abcd", "badce")

    assert isinstance(result, str)
    assert len(result) == 1


def test_find_excess_letter_result_is_the_added_character():
    a = "aabc"
    b = "cabaa"

    result = Solution().find_excess_letter(a, b)

    assert b.count(result) == a.count(result) + 1
