from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ht = Counter(nums)
        
        for x in ht:
            if ht[x] == 1:
                return x
        