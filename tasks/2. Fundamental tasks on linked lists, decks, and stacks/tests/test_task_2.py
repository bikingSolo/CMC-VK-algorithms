import pytest
from task_2 import LinkedList, Solution


def build_linked_list(values):
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1], 1),
        ([1, 2], 2),              # важно: берём "правую" середину
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30, 40, 50, 60], 40),
    ],
    ids=[
        "single",
        "two_elements_right_middle",
        "odd_length",
        "even_length",
        "odd_long",
        "even_long",
    ],
)
def test_find_middle(values, expected):
    ll = build_linked_list(values)

    middle = Solution().find_middle(ll)

    assert middle.val == expected


def test_empty_list():
    ll = build_linked_list([])

    middle = Solution().find_middle(ll)

    assert middle is None


def test_returns_actual_node_from_list():
    ll = build_linked_list([1, 2, 3, 4, 5])

    middle = Solution().find_middle(ll)

    # проверяем, что это именно узел из списка, а не новый объект
    cur = ll.head
    nodes = []
    while cur:
        nodes.append(cur)
        cur = cur.next

    assert middle in nodes


def test_structure_not_modified():
    ll = build_linked_list([1, 2, 3, 4])

    before = str(ll)

    Solution().find_middle(ll)

    after = str(ll)

    assert before == after