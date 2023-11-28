class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # To sotere no.of combinations for each target value
        dp = [0] * ( target + 1 )
        
        # only one way, to make a target
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    # based on sum of combinations from the previous target values
                    dp[i] += dp[i-num]
                    
        return dp[target]
    
    # T.C: O(target * len(nums))
    # S.C: O(target) , O(N), dp array
    