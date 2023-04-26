#User function Template for python3


#Python3
def maxSum(arr,n):

    ans=0
    arr.sort()

    i=0
    j=n-1

    while i<=j:
        ans+=abs(arr[i]-arr[j])
        i+=1
        j-=1
        
    return ans*2



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int,input().split()))
    ans=maxSum(arr,n)
    print(ans)

# } Driver Code Ends