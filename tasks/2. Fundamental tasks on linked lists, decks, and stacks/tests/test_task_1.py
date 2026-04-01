import pytest
from task_1 import LinkedList, Solution


def build_linked_list(values):
    ll = LinkedList()
    for v in values:
        ll.append(v)
    return ll


def to_list(linked_list):
    result = []
    cur = linked_list.head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def get_nodes(linked_list):
    nodes = []
    cur = linked_list.head
    while cur:
        nodes.append(cur)
        cur = cur.next
    return nodes


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        ([10, 20], [20, 10]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 2, 3], [3, 2, 2, 1]),
    ],
    ids=[
        "empty",
        "single",
        "two_elements",
        "multiple_elements",
        "duplicates",
    ],
)
def test_reverse_linked_list(values, expected):
    ll = build_linked_list(values)

    Solution().reverse_linked_list(ll)

    assert to_list(ll) == expected
    assert len(ll) == len(values)


def test_in_place_reversal():
    ll = build_linked_list([1, 2, 3])
    original_nodes = get_nodes(ll)

    Solution().reverse_linked_list(ll)

    reversed_nodes = get_nodes(ll)

    assert reversed_nodes == original_nodes[::-1]


def test_old_head_becomes_tail():
    ll = build_linked_list([1, 2, 3, 4])
    old_head = ll.head

    Solution().reverse_linked_list(ll)

    cur = ll.head
    while cur.next:
        cur = cur.next

    assert cur is old_head
    assert cur.next is None