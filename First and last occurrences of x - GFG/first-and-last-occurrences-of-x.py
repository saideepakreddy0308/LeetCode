#User function Template for python3


def find(arr,n,x):
    # code here
    # Another approach - Binary Search in O(logN) t.c
    
    first_occurrence = -1
    last_occurrence = -1
    
    # given n,x
    
    # Find first occurence
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first_occurrence = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    # Find last occurrence
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last_occurrence = mid
            low = mid + 1
            
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return first_occurrence, last_occurrence

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