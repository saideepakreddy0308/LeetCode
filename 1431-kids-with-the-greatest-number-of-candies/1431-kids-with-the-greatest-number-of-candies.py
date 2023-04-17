class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Brute Force Approach / Ad Hoc approach
        # We first find out , which kid have greatest number of candies (high)
        high = max(candies)  # O(N)
        n = len(candies)
        
        answer = []   
        
        for i in range(n):   # O(N)
            if candies[i] + extraCandies < high:
                answer.append(False)
            else:
                answer.append(True)
        return answer
    
    # Time complexity: O(N)
    # Space Complexity: O(1), The list we return is the auxiliary space and we never count auxiliary space when calculating space complexity