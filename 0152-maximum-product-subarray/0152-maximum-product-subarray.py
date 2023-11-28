class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        
        # dp arrays
        max_product = [0] * n
        min_product = [0] * n
        
        max_product[0] = nums[0]
        min_product[0] = nums[0]
        
        #update dp arrays
        
        for i in range(1,n):
            
            if nums[i] > 0:
                max_product[i] = max(nums[i],max_product[i-1]*nums[i])
                min_product[i] = min(nums[i], min_product[i-1]*nums[i])
            elif nums[i] < 0:
                max_product[i] = max(nums[i],min_product[i-1]*nums[i])
                min_product[i] = min(nums[i],max_product[i-1]*nums[i])
            else:
                max_product[i] = min_product[i] = 0
        
        return max(max_product)
    
    # T.C: O(n)
    # S.C: O(n)