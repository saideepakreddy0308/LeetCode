class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s:
            return 0
        
        n = len(s)
        # dp, to store the number of ways to decode the string up to current index
        dp = [0] * (n + 1)
        
        dp[0] = 1

        
        for i in range(1,n+1):
            
            # Add its individual
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            # Looking if it would form a 2-digit number, with current being at units place.    
            if i > 1 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
            
        return dp[n]
        