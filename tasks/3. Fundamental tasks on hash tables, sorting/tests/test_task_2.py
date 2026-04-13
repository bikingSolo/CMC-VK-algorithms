import importlib.util
from pathlib import Path

import pytest


TASK_PATH = Path(__file__).resolve().parents[1] / "task_2.py"
SPEC = importlib.util.spec_from_file_location("task_2_module", TASK_PATH)
TASK_MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(TASK_MODULE)
Solution = TASK_MODULE.Solution


def copies_done_by_time(total_time, x, y):
    first_copy_time = min(x, y)
    if total_time < first_copy_time:
        return 0

    remaining_time = total_time - first_copy_time
    return 1 + remaining_time // x + remaining_time // y


@pytest.mark.parametrize(
    "x,y,n,expected",
    [
        (1, 1, 1, 1),
        (1, 1, 2, 2),
        (1, 1, 3, 2),
        (1, 2, 1, 1),
        (1, 2, 2, 2),
        (1, 2, 4, 3),
        (2, 3, 5, 8),
        (3, 5, 4, 9),
        (4, 7, 6, 18),
        (5, 5, 10, 30),
        (10, 1, 6, 6),
        (2, 100, 3, 6),
    ],
    ids=[
        "single_copy_same_speed",
        "two_copies_same_speed",
        "three_copies_same_speed",
        "single_copy_different_speed",
        "two_copies_different_speed",
        "fast_and_slow_printer",
        "small_mixed_case",
        "medium_case",
        "larger_case",
        "equal_speeds",
        "very_fast_second_printer",
        "very_slow_second_printer",
    ],
)
def test_find_min_time_returns_expected_result(x, y, n, expected):
    assert Solution().find_min_time(x, y, n) == expected


@pytest.mark.parametrize(
    "x,y,n",
    [
        (1, 1, 2),
        (1, 1, 5),
        (1, 2, 4),
        (2, 3, 5),
        (3, 7, 8),
        (5, 11, 9),
    ],
)
def test_find_min_time_is_minimal(x, y, n):
    result = Solution().find_min_time(x, y, n)

    assert copies_done_by_time(result, x, y) >= n
    assert result == 0 or copies_done_by_time(result - 1, x, y) < n


def test_find_min_time_depends_on_first_copy_before_parallel_work():
    result = Solution().find_min_time(1, 1, 2)

    assert result == 2
