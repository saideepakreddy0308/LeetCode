class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag
        n = len(nums)
        start = 0  # holds 0
        mid = 0   # holds 1
        end = n-1   # holds 2
        
        while mid <= end:
            if nums[mid] < 1:
                nums[mid],nums[start] = nums[start],nums[mid]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[end] = nums[end],nums[mid] 
                end -= 1
                
        return nums
        