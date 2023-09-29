#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(0,i):
                x = (j + i )%2 
                print('{0} '.format(x),end='')
            print('')
        


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