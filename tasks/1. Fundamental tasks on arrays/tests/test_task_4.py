import pytest
from task_4 import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1]),
        ([0, 0, 0, 1, 1], [0, 0, 0, 1, 1]),
        ([1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1]),
        ([0], [0]),
        ([1], [1]),
        ([], []),
        ([1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1]),
    ],
)
def test_sort_binary(nums, expected):
    sol = Solution()

    result = sol.sort_binary(nums)

    assert result is None
    assert nums == expected


def test_sort_binary_in_place():
    nums = [1, 0, 1, 0]
    sol = Solution()

    original_id = id(nums)
    sol.sort_binary(nums)

    assert id(nums) == original_id
    assert nums == [0, 0, 1, 1]


def test_sort_binary_preserves_length():
    nums = [1, 0, 1, 0, 1]
    sol = Solution()

    sol.sort_binary(nums)

    assert len(nums) == 5


def test_sort_binary_sorted_property():
    nums = [1, 0, 1, 0, 0, 1]
    sol = Solution()

    sol.sort_binary(nums)

    seen_one = False
    for x in nums:
        if x == 1:
            seen_one = True
        if seen_one:
            assert x == 1
