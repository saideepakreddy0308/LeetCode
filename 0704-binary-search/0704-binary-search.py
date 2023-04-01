class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Looking for target in the array, we look into insert position where we can put target, in without disrupting order
        # Concept:  Find Upper Bound
        
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        if left > 0 and nums[left-1] == target:
            return left - 1
        else:
            return -1
        
    # Time Complexity: O(logn)
    # Space Complexity: O(1)