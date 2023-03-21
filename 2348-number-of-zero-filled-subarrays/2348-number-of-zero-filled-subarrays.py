class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_amount = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                left = right + 1
                continue
            if nums[right] == 0:
                total_amount += right - left + 1
                
        return total_amount
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)