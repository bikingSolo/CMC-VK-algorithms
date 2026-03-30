import pytest
from task_2 import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        # базовый кейс
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),

        # один массив пустой
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),

        # оба пустые
        ([], [], []),

        # одинаковые элементы
        ([1, 2, 2], [2, 2, 3], [1, 2, 2, 2, 2, 3]),

        # все элементы nums1 меньше
        ([1, 2, 3], [10, 20], [1, 2, 3, 10, 20]),

        # все элементы nums2 меньше
        ([10, 20], [1, 2, 3], [1, 2, 3, 10, 20]),

        # отрицательные числа
        ([-5, -3, -1], [-4, -2, 0], [-5, -4, -3, -2, -1, 0]),

        # разная длина массивов
        ([1], [2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [6], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_merge(nums1, nums2, expected):
    sol = Solution()
    result = sol.merge(nums1, nums2)

    assert result == expected


def test_merge_does_not_modify_inputs():
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]

    sol = Solution()
    sol.merge(nums1, nums2)

    assert nums1 == [1, 3, 5]
    assert nums2 == [2, 4, 6]


def test_merge_sorted_result():
    nums1 = [1, 4, 7]
    nums2 = [2, 3, 6]

    sol = Solution()
    result = sol.merge(nums1, nums2)

    assert result == sorted(nums1 + nums2)


def test_merge_single_elements():
    sol = Solution()

    assert sol.merge([1], [2]) == [1, 2]
    assert sol.merge([2], [1]) == [1, 2]