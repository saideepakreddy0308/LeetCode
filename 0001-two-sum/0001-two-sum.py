class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Table Approach - 2
        ht = {}
        for i,num in enumerate(nums):
            if (target - num) in ht:
                return [ht[target-num],i]
            else:
                ht[num] = i
        return []