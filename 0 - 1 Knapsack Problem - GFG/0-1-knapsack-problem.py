#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        # 2D array to store results for subproblems
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        # Compute results for subproblems iteratively
        for i in range(1,n+1):
            for w in range(1, W+1):
                # If the current item fit into the remaining weight limit
                if wt[i-1] <= w:
                    # Take maximum value between including and excluding current item
                    # To make second part positive, or else undefined
                    dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
                else:
                    # If current item cannot fit in the remaining weight limit
                    # take value from previous row
                    dp[i][w] = dp[i-1][w]
        
        # Return the full weight limit
        return dp[n][W]
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends