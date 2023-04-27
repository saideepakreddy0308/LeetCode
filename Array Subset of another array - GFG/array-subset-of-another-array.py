#User function Template for python3

def isSubset( a1, a2, n, m):
    
    ht1 = dict()
    ht2 = dict()

    for i in range(n):
        ht1[a1[i]] =  ht1.get(a1[i],0) + 1
    
    for j in range(m):
        ht2[a2[j]] =  ht2.get(a2[j],0) + 1
        
    # Comparing
    for i in ht2.keys() :
        if i in ht1 and ht1[i] >= ht2[i]:
            continue
        else:
            return "No"
    return "Yes" 
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends