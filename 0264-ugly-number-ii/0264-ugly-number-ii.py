class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [0] * n
        dp[0] = 1 # first ugly number to inert is 1.
        p2,p3,p5 = 0,0,0 # for tracking positions of ugly number

        for i in range(1, n):
            ugly2, ugly3, ugly5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            
            dp[i] = min(ugly2,ugly3,ugly5)
            
            print(dp[i],'ugly2',ugly2,'ugly3',ugly3,'ugly5',ugly5)
            # Observe for n = 10, we see ugly2 = 6, ugly3 = 6, at that time, we see the increment of both.

            if dp[i] == ugly2:
                p2 += 1
            if dp[i] == ugly3:
                p3 += 1
            if dp[i] == ugly5:
                p5 += 1
            
            print('dp[i]:', dp[i], p2,p3,p5)
        return dp[-1]
