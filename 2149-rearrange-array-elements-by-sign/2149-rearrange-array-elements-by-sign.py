class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Partition array into positive and negative numbers
        pos_nums = [x for x in nums if x > 0]
        neg_nums = [x for x in nums if x < 0]
        
        # Initialize result array
        result = []
        
        # Merge arrays, alternating between positive and negative numbers
        for p, n in zip(pos_nums, neg_nums):
            result.extend([p, n])
        
        return result