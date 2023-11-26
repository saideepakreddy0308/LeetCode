class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        
        # Check if a valid tour is possible
        if sum(diff) < 0:
            return -1
        
        # Find the start point
        start = 0
        tank = 0
        
        for i in range(n):
            tank += diff[i]
            
            # If tank goes negative, reset starting point
            if tank < 0:
                tank = 0
                start = i + 1
                
        # Check for a complete tour
        for i in range(n):
            tank += diff[(start + i) % n]
            if tank < 0:
                return -1
            
        return start
        
        # T.C: O(n), single pass through the array
        # S.C: O(n), due to 'diff' array