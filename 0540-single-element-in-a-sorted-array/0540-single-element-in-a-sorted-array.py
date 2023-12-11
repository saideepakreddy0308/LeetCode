class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums)-1
        
        while low < high:
            
            mid = (low + high) // 2
            
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1] and nums[mid] != nums[mid+1]:
                    high = mid
                elif nums[mid] != nums[mid-1] and nums[mid] == nums[mid+1]:
                    low = mid
            if mid % 2 != 0:
                if nums[mid] == nums[mid-1] and nums[mid] != nums[mid+1]:
                    low = mid + 1
                elif nums[mid] != nums[mid-1] and nums[mid] == nums[mid+1]:
                    high = mid - 1
        return nums[low]