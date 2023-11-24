from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        # Given non-overlapping intervals
        for i in range(len(intervals)):
            
            # Case 1: If not overlapping
            
            # If newInterval ends before the current interval starts, insert newInterval and return result
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # If newInterval starts after the current interval ends, keep the current interval in the result
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Case 2: If overlapping
            # If there is an overlap between newInterval and the current interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
     
        res.append(newInterval) # make sure to execute after the loop
        return res
    
# T.C: O(1)
# S.C: O(1)