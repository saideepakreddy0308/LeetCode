#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1,N):
            print('* '*i)
        for j in range(N,0,-1):
            print('* '*j)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends