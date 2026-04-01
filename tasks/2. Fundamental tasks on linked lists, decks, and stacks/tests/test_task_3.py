import pytest
from task_3 import LinkedList, Solution


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
    "values, val_to_remove, expected",
    [
        ([1, 2, 3], 2, [1, 3]),
        ([1, 2, 3], 1, [2, 3]),          # удаление головы
        ([1, 2, 3], 3, [1, 2]),          # удаление хвоста
        ([1, 2, 2, 3], 2, [1, 3]),       # несколько элементов
        ([1, 1, 1], 1, []),              # все элементы
        ([1, 2, 3], 4, [1, 2, 3]),       # нет такого значения
        ([], 1, []),                     # пустой список
    ],
    ids=[
        "remove_middle",
        "remove_head",
        "remove_tail",
        "remove_duplicates",
        "remove_all",
        "value_not_found",
        "empty_list",
    ],
)
def test_remove_val(values, val_to_remove, expected):
    ll = build_linked_list(values)

    Solution().remove_val(ll, val_to_remove)

    assert to_list(ll) == expected


def test_head_updated_correctly():
    ll = build_linked_list([1, 2, 3])

    Solution().remove_val(ll, 1)

    assert ll.head.val == 2


def test_in_place_nodes():
    ll = build_linked_list([1, 2, 3])
    original_nodes = get_nodes(ll)

    Solution().remove_val(ll, 2)

    new_nodes = get_nodes(ll)

    # проверяем, что узлы не создавались заново
    assert all(node in original_nodes for node in new_nodes)


def test_remove_consecutive_nodes():
    ll = build_linked_list([1, 2, 2, 2, 3])

    Solution().remove_val(ll, 2)

    assert to_list(ll) == [1, 3]


def test_single_element_removed():
    ll = build_linked_list([1])

    Solution().remove_val(ll, 1)

    assert ll.head is None