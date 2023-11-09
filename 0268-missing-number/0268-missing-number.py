class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    
        n = len(nums)
        
        s1 = n * (n+1) // 2
        for x in nums:
            s1 = s1 - x
        
        return s1