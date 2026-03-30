'''
## 2. Слияние двух отсортированных массивов

Дано два отсортированных массива.
Необходимо написать функцию, которая объединит эти два массива в один отсортированный.

**Что нужно сделать:**
Реализуйте алгоритм слияния, используя подход двух указателей.
Убедитесь, что итоговый массив сохраняет корректный порядок элементов.
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], nums2: List[int]):
        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        result.extend(nums1[i:])
        result.extend(nums2[j:])

        return result
