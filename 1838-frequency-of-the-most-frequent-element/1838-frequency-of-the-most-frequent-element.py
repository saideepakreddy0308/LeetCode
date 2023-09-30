class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        tot = 0
        i = 0
        ans = 0
        
        for j in range(len(nums)):
            tot += nums[j]
            while tot + k < nums[j] * (j - i + 1):
                tot -= nums[i]
                i += 1
            ans = max(ans,(j - i + 1))
        
        return ans