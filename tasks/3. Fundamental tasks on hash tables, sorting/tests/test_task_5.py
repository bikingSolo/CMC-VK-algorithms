import importlib.util
from pathlib import Path

import pytest


TASK_PATH = Path(__file__).resolve().parents[1] / "task_5.py"
SPEC = importlib.util.spec_from_file_location("task_5_module", TASK_PATH)
TASK_MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(TASK_MODULE)
Solution = TASK_MODULE.Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [1, 0]),
        ([3, 2, 4], 6, [2, 1]),
        ([3, 3], 6, [1, 0]),
        ([1, 5, 3, 7], 8, [2, 1]),
        ([0, 4, 3, 0], 0, [3, 0]),
        ([-1, -2, -3, -4, -5], -8, [4, 2]),
        ([10, -2, 8, 1], 9, [3, 2]),
        ([1], 2, []),
        ([], 10, []),
        ([1, 2, 3], 100, []),
    ],
    ids=[
        "classic_case",
        "unordered_pair",
        "duplicate_values",
        "middle_elements",
        "zeros",
        "negative_numbers",
        "mixed_signs",
        "single_element",
        "empty_list",
        "no_solution",
    ],
)
def test_find_sum(nums, target, expected):
    assert Solution().find_sum(nums, target) == expected


@pytest.mark.parametrize(
    "nums,target",
    [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([0, 4, 3, 0], 0),
        ([-1, -2, -3, -4, -5], -8),
    ],
)
def test_find_sum_returns_two_distinct_indices_with_correct_sum(nums, target):
    result = Solution().find_sum(nums, target)

    assert len(result) == 2
    assert result[0] != result[1]
    assert nums[result[0]] + nums[result[1]] == target


def test_find_sum_returns_empty_list_when_pair_is_absent():
    result = Solution().find_sum([5, 10, 15], 1)

    assert result == []
