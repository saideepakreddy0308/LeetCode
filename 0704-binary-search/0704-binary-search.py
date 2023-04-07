import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the insertion position `idx`.
        # This method uses lower_bound or bisect.bisect_left
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1
        
        # T.C : O(logN)
        # S.C : O(1)
# The bisect.bisect_left function also returns the position in the array where the target value could be inserted without disrupting the sorted order of the array, but it returns the index of the first element that is greater than or equal to the target.

# After finding the insertion position of the target, we check if the element at the index idx is equal to the target. If it is, we return the index idx because it is the index of the first occurrence of the target in the array. If it isn't, we return -1 to indicate that the target value is not present in the array.