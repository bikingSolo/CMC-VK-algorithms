import pytest
from task_7 import Solution


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 3, 3, 3, 4], [1, 2, 3, 4]),

        ([1], [1]),              # один элемент
        ([], []),                # пустой массив

        ([0, 0, 0, 1, 1, 2], [0, 1, 2]),
        ([-3, -3, -2, -1, -1], [-3, -2, -1]),

        ([1, 2, 2, 2, 2, 3], [1, 2, 3]),
        ([5, 5, 5, 5, 5], [5]),
    ],
    ids=[
        "basic",
        "all_duplicates",
        "no_duplicates",
        "mixed",

        "single",
        "empty",

        "zeros_and_duplicates",
        "negative_numbers",

        "many_duplicates_middle",
        "all_same",
    ],
)
def test_deduplicate(arr, expected):
    Solution().deduplicate(arr)

    assert arr == expected


def test_in_place_modification():
    arr = [1, 1, 2, 2, 3]
    original_id = id(arr)

    Solution().deduplicate(arr)

    assert id(arr) == original_id


def test_length_reduction():
    arr = [1, 1, 1, 2, 2, 3]

    Solution().deduplicate(arr)

    assert len(arr) == 3


def test_no_side_effect_on_unique():
    arr = [1, 2, 3, 4]

    Solution().deduplicate(arr)

    assert arr == [1, 2, 3, 4]