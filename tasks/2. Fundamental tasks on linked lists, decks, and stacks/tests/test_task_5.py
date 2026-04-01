import pytest
from task_5 import Solution


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 4, 5], 6, True),     # 1+5
        ([1, 2, 3, 4, 5], 9, True),     # 4+5
        ([1, 2, 3, 4, 5], 2, False),    # нет пары
        ([1, 2, 3, 4, 5], 10, False),   # слишком большая сумма

        ([1, 1, 3, 5], 2, True),        # одинаковые элементы
        ([1, 1, 1, 1], 2, True),        # много одинаковых
        ([1, 1, 1, 1], 3, False),

        ([-5, -2, 0, 3, 7], 1, True),   # отрицательные + положительные
        ([-5, -2, 0, 3, 7], -7, True),  # два отрицательных
        ([-5, -2, 0, 3, 7], 100, False),

        ([1, 2], 3, True),              # минимальный размер
        ([1, 2], 4, False),

        ([1], 1, False),                # один элемент
        ([], 1, False),                 # пустой массив
    ],
    ids=[
        "basic_true",
        "end_pair",
        "no_pair_small",
        "no_pair_large",

        "duplicates_pair",
        "all_duplicates_true",
        "all_duplicates_false",

        "mixed_numbers",
        "two_negatives",
        "no_pair_mixed",

        "two_elements_true",
        "two_elements_false",

        "single_element",
        "empty_array",
    ],
)
def test_find_target(arr, target, expected):
    assert Solution.find_target(arr, target) == expected