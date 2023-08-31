#User function Template for python3

def isSubset( a1, a2, n, m):
    ht1 = {}
    ht2 = {}
    for i in a1:
        ht1[i] = ht1.get(i,0) + 1
    for i in a2:
        ht2[i] = ht2.get(i,0) + 1
        
    for i in a2:
        if i not in ht1:
            return "No"
        elif i in ht1:
            ht1[i] -= 1
            if ht1[i] == 0:
                del ht1[i]
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