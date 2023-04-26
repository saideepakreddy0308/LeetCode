#User function Template for python3


def maxSum(a,n):
    # code here
    a.sort()
    sum1 = 0
    
    for i in range(n):
        sum1 += abs(a[i] - a[-i-1])
    return(sum1)

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