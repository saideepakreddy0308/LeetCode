class Solution:
    def fib(self, n: int) -> int:
        
        # Top Down Approach; Memoization - Recursion
        memo = {}
        def fn(n,memo):
            if n == 0 or n == 1:
                return n
            if n in memo:
                return memo[n]
            result = fn(n-1,memo) + fn(n-2,memo)
            
            memo[n] = result
            return result
        return fn(n,memo)
    
    # Time Complexity: O(N)
        # This is because each Fibonacci number from 0 to n is calculated only once and stored in the memoization table (dictionary) for future reference. Subsequent calculations for the same Fibonacci numbers are retrieved from the memoization table in constant time.
    # Space Complexity: O(N)