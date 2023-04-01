class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set left and right pointers
        left = 0
        right = len(nums) - 1
        
        # Under this condition
        while left <= right:
            # Get mid index
            mid = (left + right) // 2
            # Case-1
            if nums[mid] == target:
                return mid
            # Case-2
            elif nums[mid] < target:
                left = mid + 1
            # Case-3
            else:
                right = mid - 1
        # If not found
        return -1
    
    # Time Complexity: O(log n)
    # Space Complexity: O(1)