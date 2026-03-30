import pytest
from task_7 import Solution


@pytest.mark.parametrize(
    "nums",
    [
        [1, 0, 2, 0, 3, 4],
        [1, 2, 3, 0, 0],
        [0, 0, 1, 2, 3],
        [0, 1, 0, 2, 0, 3],
        [0, 0, 0],
        [1, 2, 3],
        [0],
        [5],
        [],
        [-1, 0, -2, 0, 3],
        [4, 0, 4, 0, 4],
        [7, 0, 1, 0, 9, 0, 2],
    ],
)
def test_move_zeros(nums):
    sol = Solution()

    original = nums[:]
    original_id = id(nums)
    zero_count = original.count(0)
    non_zero_before = sorted(x for x in original if x != 0)

    result = sol.move_zeros(nums)

    assert result is None
    assert id(nums) == original_id
    assert len(nums) == len(original)
    assert nums.count(0) == zero_count
    assert sorted(x for x in nums if x != 0) == non_zero_before

    if zero_count > 0:
        assert nums[-zero_count:] == [0] * zero_count


def test_move_zeros_all_non_zero_prefix():
    nums = [4, 0, 1, 0, 3, 0, 2]
    sol = Solution()

    zero_count = nums.count(0)
    sol.move_zeros(nums)

    if zero_count < len(nums):
        assert all(x != 0 for x in nums[:-zero_count])


def test_move_zeros_empty():
    nums = []
    sol = Solution()

    result = sol.move_zeros(nums)

    assert result is None
    assert nums == []