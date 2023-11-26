class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_len = 1
        
        for num in nums:
            # Check if the current number is the start of a new consecutive sequence
            if num - 1 not in num_set:
                current_num = num
                current_len = 1
                
                # Extend the consecutive sequence by checking for consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1
                
                max_len = max(max_len, current_len)
        
        return max_len

    # T.C: O(N), here each elt is processed once, and in worst case, each elt part of only one consecutive sequence
    # S.C: O(n) due to Hashset