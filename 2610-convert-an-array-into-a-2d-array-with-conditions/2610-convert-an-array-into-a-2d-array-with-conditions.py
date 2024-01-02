from collections import Counter
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ht = Counter(nums)
        result = []

        x = max(ht.values())

        for _ in range(x):
            l = []
            for key, value in ht.items():
                if value >= 1:
                    l.append(key)
                    ht[key] -= 1
            result.append(l)

        return result
    
# t.c: O(x * n), x is max.val of a single no, and n is no.of unique elts in ht
# s.c: O(n)