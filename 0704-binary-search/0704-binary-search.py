class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # APPROACH - 3 (lower bound)
        # Looking for target in the array, and insert into the positon where we can put target without disrupting order
        # Looking for left most insert position
        
        l = 0
        r = len(nums)
        
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if l < len(nums) and nums[l] == target:
            return l
        else:
            return -1
        
        # T.C: O(logN)
        # S.C: O(1)