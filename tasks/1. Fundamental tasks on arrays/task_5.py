'''
## 5. Задача флага Нидерландов

Дан массив, состоящий из 0, 1 и 2.
Необходимо отсортировать его за линейное время.
**Аналог задачи:** Sort Colors (LeetCode)
<https://leetcode.com/problems/sort-colors/description/>
Реализуйте алгоритм трёх указателей (Dutch National Flag).
Кратко опишите, как поддерживаются границы для 0, 1 и 2 во время прохода по массиву.

Решение:
1. За левой границей всегда находятся нули. `Левая граница растет вместе со средним индексом, поэтому средний не выходит за нее
2. За правой границей всегда находятся двойки. Если средний индекс заходит за правую границу - задача решена
3. Между левой границей и средним элементом - единицы
4. Между средним и правой границей - необработанная часть
'''
from typing import List

class Solution:
    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        r = len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                self.swap(nums, l, m)
                l += 1
                m += 1
            elif nums[m] == 2:
                self.swap(nums, r, m)
                r -= 1
            else:
                m += 1