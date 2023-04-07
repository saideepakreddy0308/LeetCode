class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach - 2 ( Upper Bound)
         # We look for target in the arrat and look into insert position without distrupting order
            
            l = 0
            r = len(nums)
            
            while l < r:
                mid = l + (r-l)//2
                # Case_1:
                if nums[mid] <= target:
                    l = mid + 1
                else:  # nums[mid] > target
                    r = mid
            if l > 0 and nums[l-1] == target:
                return l - 1
            else:
                return -1 
            
        # Time Complexity: O(logN)
        # Space Complexity: O(1)