#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(N):
            print(" " * (N-i-1),end='')
            print("* " * (i+1))
        for i in range(N):
            print(" "*i,end="")
            print("* "*(N-i))
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends