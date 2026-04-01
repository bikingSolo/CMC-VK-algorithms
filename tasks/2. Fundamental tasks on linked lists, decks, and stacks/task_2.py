'''
## 2. Найти середину списка
Дан односвязный список.
Необходимо найти его середину за O(n) без дополнительных аллокаций

**Что нужно сделать:**
Используйте метод двух указателей (медленный и быстрый).
Поясните, почему быстрый указатель позволяет определить середину за один проход.

**Объяснение:**
Быстрый указатель в два раза быстрее пройдет список.
Значит когда он будет в конце - медленный будет на середине.
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
    def find_middle(self, linked_list: LinkedList):
        slow = linked_list.head
        fast = linked_list.head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow
