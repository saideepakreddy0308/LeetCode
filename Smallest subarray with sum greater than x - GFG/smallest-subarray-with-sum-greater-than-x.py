class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        window_start = 0
        curr_sum = 0
        min_length = float('inf')
        
        for window_end in range(n):
            curr_sum += a[window_end]
            
            while curr_sum > x:
                min_length = min(min_length, window_end - window_start + 1)
                curr_sum -= a[window_start]
                window_start += 1
        
        return min_length if min_length != float('inf') else 0

#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends