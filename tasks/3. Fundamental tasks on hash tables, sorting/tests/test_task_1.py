import importlib.util
from pathlib import Path

import pytest


TASK_PATH = Path(__file__).resolve().parents[1] / "task_1.py"
SPEC = importlib.util.spec_from_file_location("task_1_module", TASK_PATH)
TASK_MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(TASK_MODULE)
Solution = TASK_MODULE.Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (17, 4),
        (24, 4),
        (26, 5),
        (99, 9),
        (10**6, 1000),
        (2147395599, 46339),
        (2147395600, 46340),
    ],
    ids=[
        "zero",
        "one",
        "two",
        "three",
        "four",
        "eight",
        "perfect_square_9",
        "before_16",
        "perfect_square_16",
        "after_16",
        "before_25",
        "after_25",
        "two_digit_number",
        "one_million",
        "large_non_square",
        "large_perfect_square",
    ],
)
def test_sqrt_returns_integer_part_of_square_root(n, expected):
    assert Solution().sqrt(n) == expected


@pytest.mark.parametrize(
    "n",
    [0, 1, 2, 5, 10, 24, 25, 26, 999, 10**6 + 123],
)
def test_sqrt_result_satisfies_floor_root_property(n):
    result = Solution().sqrt(n)

    assert result * result <= n
    assert (result + 1) * (result + 1) > n


def test_sqrt_returns_int():
    result = Solution().sqrt(12345)

    assert isinstance(result, int)
