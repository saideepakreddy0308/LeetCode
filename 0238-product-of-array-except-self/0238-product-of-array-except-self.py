class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = [1] * n
        
        # Left pass
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        # Right pass
        right_product = 1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
    
   # T.C: O(n)
   # S.c: O(n)
   # no division operation is used here
        