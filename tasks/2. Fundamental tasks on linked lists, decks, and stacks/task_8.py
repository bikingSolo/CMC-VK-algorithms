'''
## 8. Слияние двух отсортированных списков

Написать функцию, которая принимает два отсортированных односвязных списка
и объединяет их в один отсортированный список.
Затраты по памяти должны быть O(1).

Входные данные:
list1 = [3, 6, 8]
list2 = [4, 7, 9, 11]

Выходные данные:
[3, 4, 6, 7, 8, 9, 11]

**Что нужно сделать:**
Реализуйте слияние, изменяя только ссылки между существующими узлами.
Объясните, почему алгоритм работает за O(n + m) и не требует дополнительной памяти.

**Объяснение:**
1. Потому-что мы одновременно идем по обоим спискам и сравниваем их элементы.
    1.1. Если элемент второго списка оказался меньше - мы вставляем его ровно за ныншеним элементом первого списка. После чего идем дальше по второму списку.
    1.2. Если наоборот больше - мы идем дальше по первому списку (т.к. не можем вставить спереди - мы не знаем, будет ли следующий элемент первого списка больше).
    1.3. Так пока не закончится один из списков. Если первым кончился первый список - оставшиеся элементы второго мы вставляем в конец первого.
    1.4. Итого - один проход по каждому списку + вставки за O(1) - O(n + m)
2. Для того, чтобы вставлять элементы перед нынешним - нужна ссылка на предыдущий. Его мы инициализаируем dummy переменной (ссылкой на head).
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
    def merge_two_lists(self, list1: LinkedList, list2: LinkedList):
        dummy = Node(None)
        dummy.next = list1.head

        i_prev = dummy
        i = list1.head
        j = list2.head

        while i is not None and j is not None:
            if i.val > j.val:
                i_prev.next = j
                next = j.next
                j.next = i
                i_prev = j
                j = next
            else:
                i_prev = i
                i = i.next

            
        while j is not None:
            i_prev.next = j
            i_prev = j
            j = j.next

        list1.head = dummy.next