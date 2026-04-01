'''
## 3. Удалить элемент из односвязного списка
Необходимо написать функцию, которая принимает односвязный список и целое число val.
Нужно удалить узел, значение которого равно val.

**Что нужно сделать:**
Реализуйте удаление узла без создания нового списка.
Объясните, как обрабатываются случаи удаления головы списка и внутренних элементов.

**Объяснение:**
1. Для корректной обработки удаления головы используем dummy указатель на голову
как инициализацию предыдущего элемента. В конце мы присваиваем голове значение dummy.next.
2. В общем случае для удаления элемента мы меняем ссылку предыдущего элемента.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        cur = self.head
        res = "["

        while cur is not None:
            if cur.next is None:
                res += f"{cur.val}"
            else:
                res += f"{cur.val}, "
            cur = cur.next

        return res + "]"

    def append(self, val):
        self.size += 1
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        
        cur.next = new_node


class Solution:
    def remove_val(self, linked_list: LinkedList, val):
        dummy = Node(None)
        dummy.next = linked_list.head

        cur = linked_list.head
        prev = dummy
        
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        linked_list.head = dummy.next