class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the insertion position `idx`.
        # This method uses upper_bound or bisect.bisect_right
        idx = bisect.bisect_right(nums, target)

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1