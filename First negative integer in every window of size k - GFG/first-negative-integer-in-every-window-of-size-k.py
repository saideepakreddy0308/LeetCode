#User function Template for python3

def printFirstNegativeInteger(A, N, K):
    q = []
    res = []
    
    for i in range(N):
        if A[i] < 0:
            q.append(i)
        
        if i >= K - 1:
            while q and q[0] < i - K + 1:
                q.pop(0)
            
            res.append(A[q[0]]) if q else res.append(0)
    
    return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends