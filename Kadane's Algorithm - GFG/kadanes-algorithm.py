#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        # Here atleast a positive number else if all are negatives , max_so_far = min[arr]
        max_so_far = arr[0]
        max_ending_here = arr[0]
        
        for i in range(1,N):
            max_so_far = max(arr[i],max_so_far + arr[i])
            max_ending_here = max(max_ending_here, max_so_far)
        
        return max_ending_here

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends