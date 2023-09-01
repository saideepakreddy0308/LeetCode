
class Solution:
    def minSubset(self, arr,n):
        arr.sort()
        total=sum(arr)
        i=n-1
        res=[]
        s=0
        while(i>=0):
            s+=arr[i]
            total-=arr[i]
            if(s>total):
                return n-i
            i-=1
        return n
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A,N)
        print(ans)
# } Driver Code Ends