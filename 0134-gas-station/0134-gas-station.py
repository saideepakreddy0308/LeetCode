class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0
        current_diff = 0
        start = 0
        
        for i in range(len(gas)):
            total_diff += gas[i] - cost[i]
            current_diff += gas[i] - cost[i]
            
            if current_diff < 0:
                # If the current difference is negative, reset starting point
                current_diff = 0
                start = i + 1
                
        return start if total_diff >= 0 else -1