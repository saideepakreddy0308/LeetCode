class Solution:
    def fib(self, n: int) -> int:
        
        # Bottom up Approach; Tabulation - Iterative
        # Creating array named dp
        if n == 0:
            return 0
        
        dp = [0] * (n+1)
        # Base Cases
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]
    
    # Time Complexity: O(N)
        # This is because each Fibonacci number from 0 to n is calculated only once and stored in the memoization table (dictionary) for future reference. Subsequent calculations for the same Fibonacci numbers are retrieved from the memoization table in constant time.
    # Space Complexity: O(N)