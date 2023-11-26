class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[1]) # sort based on end points
        count = 1 # count of non-overlapping intervals
        end = intervals[0][1] # End point of the first interval
        
        for interval in intervals[1:]:
            start = interval[0]
            if start >= end:
                count += 1
                end = interval[1]
        return len(intervals) - count  # (here count gives the correct non-overlapping intervals)
    
        # T.C: O(nlogn)
        # S.c: O(1)
    
    # Example: after sorting, [1,2], [2,3], [1,3], [3,4]
        # end of first interval [1,2] is 2
        # Here, for [2,3], 2 is greater than equal to 2(end of first), so selected and update end to 3.
        # for [1,3], the start(1) is less than end(3) of the interval taken,so overlap, skip this interval
        # for [3,4], start(3) is equal to current end(3). Skip the interval
        
        # so final count is 1,as only one non-overlapping is removed