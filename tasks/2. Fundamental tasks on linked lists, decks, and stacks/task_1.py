'''
## 1. Развернуть односвязный список

Необходимо написать функцию, которая принимает на вход односвязный список
и разворачивает его.

**Что нужно сделать:**
Реализуйте разворот списка in-place, изменяя ссылки между узлами.
Объясните, как меняются указатели на каждом шаге и почему алгоритм работает за O(n).

**Объяснение:**
1. На каждом шаге у нас есть ссылки на предыдущий, нынешний и следующий элементы.
Ссылку на следующий элемент мы меняем на ссылку на предыдущий - тем самым разворачиваем
список. Благодаря сохраненным ссылкам мы можем пойти дальше, перед этим обновив указатели.

2. Алгоритм работает за O(n), т.к. нужен всего один проход по списку.
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
    def reverse_linked_list(self, linked_list: LinkedList):
        prev = None
        cur = linked_list.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        linked_list.head = prev
