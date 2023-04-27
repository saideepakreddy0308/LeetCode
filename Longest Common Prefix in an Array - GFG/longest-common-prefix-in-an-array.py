#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort(key = len)
        mm = arr[0]
        m = len(mm)

        for i in range(m, 0, -1):
            mn = mm[ : i]
            for j in arr:
                if j[ : i] != mn:
                    break
            else:
                return mn

        return "-1"
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends