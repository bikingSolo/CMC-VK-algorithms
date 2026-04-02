import pytest
from task_8 import LinkedList, Solution


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
    "values1, values2, expected",
    [
        ([3, 6, 8], [4, 7, 9, 11], [3, 4, 6, 7, 8, 9, 11]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([], [], []),
        ([1], [2], [1, 2]),
        ([2], [1], [1, 2]),
        ([1, 1, 3], [1, 2, 2], [1, 1, 1, 2, 2, 3]),
        ([-5, -1, 3], [-4, 0, 2], [-5, -4, -1, 0, 2, 3]),
        ([1, 4, 7], [2, 3, 5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([10, 20, 30], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 10, 20, 30])
    ],
    ids=[
        "example",
        "interleaving",
        "second_empty",
        "first_empty",
        "both_empty",
        "single_already_ordered",
        "single_need_swap",
        "duplicates",
        "negative_numbers",
        "different_lengths",
        "second_greater"
    ],
)
def test_merge_two_lists(values1, values2, expected):
    list1 = build_linked_list(values1)
    list2 = build_linked_list(values2)

    Solution().merge_two_lists(list1, list2)

    assert to_list(list1) == expected


def test_merge_is_in_place_for_existing_nodes():
    list1 = build_linked_list([1, 3, 5])
    list2 = build_linked_list([2, 4, 6])

    nodes_before = get_nodes(list1) + get_nodes(list2)

    Solution().merge_two_lists(list1, list2)

    nodes_after = get_nodes(list1)

    assert len(nodes_after) == len(nodes_before)
    assert set(map(id, nodes_after)) == set(map(id, nodes_before))


def test_result_head_is_updated():
    list1 = build_linked_list([3, 4, 5])
    list2 = build_linked_list([1, 2])

    Solution().merge_two_lists(list1, list2)

    assert list1.head.val == 1


def test_result_is_sorted():
    list1 = build_linked_list([1, 4, 7])
    list2 = build_linked_list([2, 3, 5, 6])

    Solution().merge_two_lists(list1, list2)

    result = to_list(list1)
    assert result == sorted(result)


def test_tail_ends_with_none():
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([3, 5, 6])

    Solution().merge_two_lists(list1, list2)

    cur = list1.head
    while cur.next:
        cur = cur.next

    assert cur.next is None