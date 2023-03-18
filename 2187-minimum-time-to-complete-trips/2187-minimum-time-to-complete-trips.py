class Solution:
    MAX_NUMBER_OF_TRIPS = 10_000_000
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        # set lower and upper bound
        # number of trips within lower bound is always lower than totalTrips
        low = 0
        # number of trips within upper bound is always higher or equal than totalTrips
        # O(N)
        high = min(time) * self.MAX_NUMBER_OF_TRIPS


        # binary search  # On time 
        
        while high - low > 1:   
            mid = (high + low) // 2
            # O(N)
            trips = sum( [mid//t for t in time] )
            if trips < totalTrips:
                low = mid
            else:
                high = mid

        return high

        