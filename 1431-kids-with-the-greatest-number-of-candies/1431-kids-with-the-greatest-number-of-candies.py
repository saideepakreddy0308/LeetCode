class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Brute Force Approach
        high = max(candies)
        n = len(candies)
        
        answer = []
        
        for i in range(n):
            if candies[i] + extraCandies < high:
                answer.append(False)
            else:
                answer.append(True)
        return answer