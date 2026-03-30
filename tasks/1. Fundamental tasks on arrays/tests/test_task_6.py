import pytest
from task_6 import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        # пример из условия
        ([3, 2, 4, 1, 11, 8, 9], [2, 4, 8, 1, 11, 3, 9]),

        # уже в нужном виде
        ([2, 4, 6, 1, 3, 5], [2, 4, 6, 1, 3, 5]),

        # все нечётные
        ([1, 3, 5, 7], [1, 3, 5, 7]),

        # все чётные
        ([2, 4, 6, 8], [2, 4, 6, 8]),

        # перемешанные
        ([1, 2, 3, 4, 5, 6], [2, 4, 6, 1, 5, 3]),

        # один элемент
        ([2], [2]),
        ([3], [3]),

        # пустой массив
        ([], []),

        # отрицательные числа
        ([-2, -3, -4, -1], [-2, -4, -3, -1]),

        # нули (считаются чётными)
        ([0, 1, 2, 0, 3], [0, 2, 0, 1, 3]),
    ],
)
def test_move_even(nums, expected):
    sol = Solution()

    result = sol.move_even(nums)

    assert result is None
    assert nums == expected


def test_move_even_in_place():
    nums = [1, 2, 3, 4]
    sol = Solution()

    original_id = id(nums)
    sol.move_even(nums)

    assert id(nums) == original_id
    assert nums == [2, 4, 3, 1]


def test_move_even_preserves_length():
    nums = [1, 2, 3, 4, 5]
    sol = Solution()

    sol.move_even(nums)

    assert len(nums) == 5


def test_move_even_only_reorders_elements():
    nums = [3, 2, 4, 1]
    sol = Solution()

    original_sorted = sorted(nums)
    sol.move_even(nums)

    assert sorted(nums) == original_sorted


def test_move_even_even_first_property():
    nums = [3, 2, 4, 1, 6, 5]
    sol = Solution()

    sol.move_even(nums)

    seen_odd = False
    for x in nums:
        if x % 2 != 0:
            seen_odd = True
        if seen_odd:
            assert x % 2 != 0


def test_move_even_stability_even():
    nums = [2, 4, 6, 8]
    sol = Solution()

    sol.move_even(nums)

    assert nums == [2, 4, 6, 8]


def test_move_even_stability_odd():
    nums = [1, 3, 5, 7]
    sol = Solution()

    sol.move_even(nums)

    assert nums == [1, 3, 5, 7]