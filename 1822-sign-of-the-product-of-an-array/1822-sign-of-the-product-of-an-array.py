class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Approach: Tracking sign
        
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -1 * sign
        return sign