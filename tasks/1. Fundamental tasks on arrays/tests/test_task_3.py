import pytest
from task_3 import Solution


@pytest.mark.parametrize(
    "nums1,m,nums2,n,expected",
    [
        # базовый кейс
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),

        # nums2 меньше
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),

        # nums2 пустой
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),

        # nums1 пустой (только нули)
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),

        # дубликаты
        ([1, 2, 2, 0, 0, 0], 3, [2, 2, 3], 3, [1, 2, 2, 2, 2, 3]),

        # отрицательные числа
        ([-3, -1, 0, 0, 0], 2, [-2, -1, 2], 3, [-3, -2, -1, -1, 2]),

        # разные размеры
        ([2, 0], 1, [1], 1, [1, 2]),

        # один элемент
        ([0], 0, [1], 1, [1]),
        ([1], 1, [], 0, [1]),
    ],
)
def test_merge_inplace(nums1, m, nums2, n, expected):
    sol = Solution()

    result = sol.merge(nums1, m, nums2, n)

    assert result is None
    assert nums1 == expected


def test_merge_modifies_nums1_in_place():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    sol = Solution()

    original_id = id(nums1)
    sol.merge(nums1, 3, nums2, 3)

    assert id(nums1) == original_id
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_uses_only_first_m_elements():
    nums1 = [1, 2, 3, 999, 999, 999]
    nums2 = [4, 5, 6]

    sol = Solution()
    sol.merge(nums1, 3, nums2, 3)

    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_property():
    nums1 = [1, 4, 7, 0, 0, 0]
    nums2 = [2, 3, 6]

    sol = Solution()
    sol.merge(nums1, 3, nums2, 3)

    assert nums1 == sorted([1, 4, 7] + [2, 3, 6])