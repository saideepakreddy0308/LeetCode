#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        arr.sort()
        sum = 0
        i = N - 1 #6
        while i >= 1:
            if (arr[i] - arr[i-1]) < K:
                sum += ( arr[i] + arr[i-1])
                i -= 2
            else:
                i -= 1
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends