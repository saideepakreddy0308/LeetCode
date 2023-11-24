from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two_sum -> Hash Map
        # Two_sum_II -> Left and Right Pointers
        
        # Sort and don't take duplicates, once taken, and TwoSumII = 3Sum
        
        res = []
        nums.sort()  # Sort the input array
        
        for i, a in enumerate(nums):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            # TwoSum II with left and right pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                # Adjust pointers based on the sum
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Found a triplet, add it to the result
                    res.append([a, nums[l], nums[r]])
                    
                    # Skip duplicates for the second and third elements of the triplet
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
