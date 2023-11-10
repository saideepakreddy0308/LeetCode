class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # if found as mid
            if nums[mid] == target:
                return mid
            
            # rotated 
            # 1. Check if the left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # 2. Check if the right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    # Logic behind to not search for the target with low and high end, check the side that is actually sorted and then looking into it.
        