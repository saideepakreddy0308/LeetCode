class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # APPROACH - 1
        # Initialize left and Right Pointers
        l = 0
        r = len(nums) - 1
        
        # Binary Search
        while l<=r:
            mid = (l + (r-l)//2)
            # Case_1:
            if nums[mid] == target:
                return mid
            # Case_2:
            elif nums[mid] > target:
                r = mid - 1
            # Case_3
            else:
                l = mid + 1
        return -1
    # T.C : O(logN)
    # S.C : O(1)