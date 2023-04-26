#User function Template for python3


def find(arr,n,x):
    # code here
    if n == 0:
        return [-1,-1]
    l = []
    for i in range(n):
        if arr[i] < x:
            continue
        elif arr[i] == x:
            l.append(i)
        elif arr[i] > x:
            break
    if len(l) == 0:
        return [-1,-1]
    return [l[0],l[-1]]
    
    # T.C: O(logN)
    


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends