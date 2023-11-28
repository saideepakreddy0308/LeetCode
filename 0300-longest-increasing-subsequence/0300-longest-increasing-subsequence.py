class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # Handle Special Cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Initialize dp array
        dp = [1] * n
        
        # Update the dp array
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)