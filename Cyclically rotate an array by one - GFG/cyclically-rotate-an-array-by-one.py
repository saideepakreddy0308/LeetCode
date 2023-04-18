#User function Template for python3

def rotate( arr, n):
    arr.insert(0,arr[n-1])  # insert at position 0
    arr.pop(n)  # pop from last position
    
    # arr[:] = [arr[-1]] + arr[0:-1]
    
    return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends