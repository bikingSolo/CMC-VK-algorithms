import pytest
from task_5 import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        # базовый кейс
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),

        # уже отсортирован
        ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),

        # обратный порядок
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),

        # только один тип
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2], [2, 2, 2]),

        # перемешанные
        ([1, 0, 2, 1, 0, 2], [0, 0, 1, 1, 2, 2]),

        # один элемент
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),

        # пустой массив
        ([], []),

        # сложный кейс
        ([2, 1, 0, 2, 1, 0, 1, 2, 0], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
    ],
)
def test_sort_colors(nums, expected):
    sol = Solution()

    result = sol.sortColors(nums)

    assert result is None
    assert nums == expected


def test_sort_colors_in_place():
    nums = [2, 0, 1]
    sol = Solution()

    original_id = id(nums)
    sol.sortColors(nums)

    assert id(nums) == original_id
    assert nums == [0, 1, 2]


def test_sort_colors_sorted_property():
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()

    sol.sortColors(nums)

    # проверяем порядок: сначала 0, потом 1, потом 2
    stage = 0
    for x in nums:
        if stage == 0:
            if x == 1:
                stage = 1
            elif x == 2:
                stage = 2
        elif stage == 1:
            if x == 0:
                pytest.fail("0 after 1")
            if x == 2:
                stage = 2
        else:  # stage == 2
            if x != 2:
                pytest.fail("non-2 after 2")


def test_sort_colors_preserves_length():
    nums = [2, 1, 0, 1, 2]
    sol = Solution()

    sol.sortColors(nums)

    assert len(nums) == 5


def test_sort_colors_only_valid_values():
    nums = [2, 0, 1, 2, 1, 0]
    sol = Solution()

    sol.sortColors(nums)

    assert all(x in (0, 1, 2) for x in nums)