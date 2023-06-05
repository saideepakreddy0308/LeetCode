#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # Create a dp list initialized with 0s
        dp = [0] * (Sum + 1)
        
        # There is only one way to make a sum of 0, i.e., by not choosing any coin
        dp[0] = 1
        
        # Iterate through the coins and update the dp list
        for coin in coins:
            for i in range(coin, Sum + 1):
                dp[i] += dp[i - coin]
        
        # Return the number of ways to make the sum
        return dp[Sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends