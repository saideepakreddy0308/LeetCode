#User function Template for python3

# Binary Search Method
class Solution:
    def MissingNumber(self,array,n):
        # code here
        l = 0
        r = n - 2
        
        array.sort()
        while l <= r:
            mid = l + (r-l)//2
            if array[mid] == mid + 1:
                l = mid + 1
            else:
                r = mid - 1
        return l + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends