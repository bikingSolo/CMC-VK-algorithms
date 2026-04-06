import pytest

from task_7 import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], []),
        ([0], [0]),
        ([5], [5]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 1], [1, 0]),
        ([1, 0], [1, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
        ([4, 0, 5, 0, 0, 3, 0, 1], [4, 5, 3, 1, 0, 0, 0, 0]),
        ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),
        ([0, 1, 2, 3, 0], [1, 2, 3, 0, 0]),
        ([7, 0, 0, 8, 9, 0, 10], [7, 8, 9, 10, 0, 0, 0]),
        ([0, -1, 0, -2, 3], [-1, -2, 3, 0, 0]),
    ],
)
def test_move_zeros_examples(solver, nums, expected):
    solver.move_zeros(nums)
    assert nums == expected


def test_preserves_relative_order_of_non_zero_elements(solver):
    nums = [4, 0, 2, 0, 3, 0, 1]
    expected = [4, 2, 3, 1, 0, 0, 0]

    solver.move_zeros(nums)

    assert nums == expected


def test_all_zeros_remain_in_array(solver):
    nums = [0, 0, 1, 0, 2, 0, 3, 0]
    solver.move_zeros(nums)

    assert nums.count(0) == 5
    assert nums == [1, 2, 3, 0, 0, 0, 0, 0]


def test_large_case(solver):
    nums = [0, 1] * 1000
    expected = [1] * 1000 + [0] * 1000

    solver.move_zeros(nums)

    assert nums == expected