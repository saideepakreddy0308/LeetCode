#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        left = 0
        right = n-1
        index = 0
        while left <= right:
            # if right is 2
            while arr[right] == 2 and left <= right:
                right -= 1
            # while left is 2
            if arr[left] == 2 and left <= right:
                arr[right],arr[left] = arr[left],arr[right]
                right -= 1
            # while left is 0
            if arr[left] == 0 and left <= right:
                arr[index], arr[left] = arr[left], arr[index]
                index += 1
            left += 1
        # print(*arr)


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