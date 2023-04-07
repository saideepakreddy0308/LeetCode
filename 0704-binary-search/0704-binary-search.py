class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Finding Upper bound
        idx = bisect.bisect_right(nums,target)
        
        if idx > 0 and nums[idx-1] == target:
            return idx - 1
        else:
            return -1
        
        # T.C : O(logN)
        # S.C:  O(1)
        
        # The bisect.bisect_right function returns the position in the array where the target value could be inserted without disrupting the sorted order of the array. If the target value is already present in the array, the bisect.bisect_right function returns the index of the element that is greater than the target.

# After finding the insertion position of the target, we check if the element at the index idx-1 is equal to the target. If it is, we return the index idx-1 because it is the index of the first occurrence of the target in the array. If it isn't, we return -1 to indicate that the target value is not present in the array.

# The time complexity of this solution is O(logN) because the bisect.bisect_right function uses binary search to find the insertion position of the target. The space complexity is O(1) because we only need a constant amount of extra space to store the idx variable.