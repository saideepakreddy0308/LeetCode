class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        # Thought process to work with prefix sum
        
        count = 0 # for sum count after adding at each step
        max_length = 0 # max length of contiguous array with equal no.of 0 and 1
        
        sum_index = { 0: -1}  # running sum, index
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                count -=1
            else:
                count += 1
            
            if count in sum_index:
                max_length = max(max_length, i - sum_index[count])
            else:
                sum_index[count] = i
        
        return max_length 