class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        # Approach: Prefix Sum + Greedy
        
        # Initialize result and the prefix sum
        result = 0
        prefix_sum = 0
        
        # Iterate over nums, update prefix sum and result
        for i in range(len(nums)):
            prefix_sum += nums[i]
            result = max(result,math.ceil(prefix_sum/(i+1)))
        return result