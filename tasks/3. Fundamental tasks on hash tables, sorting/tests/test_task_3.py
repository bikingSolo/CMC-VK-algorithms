import importlib.util
from pathlib import Path

import pytest


TASK_PATH = Path(__file__).resolve().parents[1] / "task_3.py"
SPEC = importlib.util.spec_from_file_location("task_3_module", TASK_PATH)
TASK_MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(TASK_MODULE)
Solution = TASK_MODULE.Solution


@pytest.mark.parametrize(
    "animals,food,expected",
    [
        ([1, 2, 3], [1, 1], 1),
        ([1, 2], [1, 2, 3], 2),
        ([2, 3, 4], [1, 2, 3], 2),
        ([2, 2, 3], [1, 2, 2, 3], 3),
        ([5, 10], [1, 2, 3], 0),
        ([1, 1, 1], [1, 1, 1], 3),
        ([4], [5], 1),
        ([5], [4], 0),
        ([3, 1, 2], [2, 1, 3], 3),
        ([1, 2, 3, 4], [2, 2, 2], 2),
        ([], [1, 2, 3], 0),
        ([1, 2, 3], [], 0),
        ([], [], 0),
    ],
    ids=[
        "not_enough_small_portions",
        "enough_for_all",
        "partial_match",
        "duplicates",
        "no_animal_can_be_fed",
        "all_equal",
        "single_success",
        "single_failure",
        "unsorted_inputs",
        "more_animals_than_food",
        "no_animals",
        "no_food",
        "both_empty",
    ],
)
def test_find_animals_amount(animals, food, expected):
    assert Solution().find_animals_amount(animals, food) == expected


def test_find_animals_amount_sorts_inputs_in_place():
    animals = [3, 1, 2]
    food = [2, 3, 1]

    Solution().find_animals_amount(animals, food)

    assert animals == [1, 2, 3]
    assert food == [1, 2, 3]


def test_find_animals_amount_result_does_not_exceed_animals_or_food_count():
    animals = [1, 2, 2, 10]
    food = [1, 2, 3]

    result = Solution().find_animals_amount(animals, food)

    assert 0 <= result <= len(animals)
    assert 0 <= result <= len(food)
