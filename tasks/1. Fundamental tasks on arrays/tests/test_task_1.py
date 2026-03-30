import pytest
from task_1 import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [5, 1, 2, 3, 4]),
        ([42], 10, [42]),
        ([1, 2], 1, [2, 1]),
        ([-1, -2, -3, -4], 2, [-3, -4, -1, -2]),
        ([10, 20, 30, 40, 50, 60], 4, [30, 40, 50, 60, 10, 20]),
        ([], 100, [])
    ],
)
def test_rotate_various_cases(nums, k, expected):
    sol = Solution()

    result = sol.rotate(nums, k)

    assert result is None
    assert nums == expected


def test_rotate_modifies_list_in_place():
    nums = [1, 2, 3, 4, 5]
    sol = Solution()

    original_id = id(nums)
    sol.rotate(nums, 2)

    assert id(nums) == original_id
    assert nums == [4, 5, 1, 2, 3]


def test_rotate_large_k():
    nums = [1, 2, 3, 4]
    sol = Solution()

    sol.rotate(nums, 10)  # 10 % 4 == 2

    assert nums == [3, 4, 1, 2]
