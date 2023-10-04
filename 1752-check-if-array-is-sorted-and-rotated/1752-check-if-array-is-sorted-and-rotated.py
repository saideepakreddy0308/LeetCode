class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0 # count of points where array decreases
        
        for i in range(n):
            # If decreasing point is found, increase the count
            if nums[i] > nums[(i+1) % n]:
                count += 1
            #If more than one decreasing point is found, return False
            if count > 1:
                return False
        
        return True