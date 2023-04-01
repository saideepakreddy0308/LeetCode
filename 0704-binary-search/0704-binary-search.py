class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Looking for target in the array, we look into insert position where we can put target, in without disrupting order
        # Concept:  Find Lower Bound, here we look for leftmost insert position        
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1
        
    # Time Complexity: O(logn)
    # Space Complexity: O(1)