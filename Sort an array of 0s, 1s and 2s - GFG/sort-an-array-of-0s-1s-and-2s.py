#User function Template for python3

class Solution:
    def sort012(self, arr, n):
        # let [a,b] = [0,2], working similar to Dutch National Flag problem
        a = 0
        b = 2
        start = 0
        mid = 0
        end = n - 1
        while mid <= end:
            if arr[mid] == 0:
                arr[start], arr[mid] = arr[mid], arr[start]
                start += 1
                mid += 1
            elif a < arr[mid] < b:
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end -= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends