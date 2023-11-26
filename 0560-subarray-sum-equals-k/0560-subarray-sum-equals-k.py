class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_count = {0:1} # initialize with running sum of 0 and count 1
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            # Check if running sum - k exists in the hashmap
            if running_sum - k in sum_count:
                count += sum_count[running_sum - k]
            # Update the hashmap with current running_sum
            sum_count[running_sum] = sum_count.get(running_sum,0) + 1
        return count
    # T.C: O(n), iterate once
    # S.C: O(n), sum_count hashmap