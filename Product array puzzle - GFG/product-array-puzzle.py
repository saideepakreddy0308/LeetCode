#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        p_nozero = 1
        count_zero = 0
        
        for i in nums:
            if i == 0:
                count_zero += 1
            else:
                p_nozero *= i
        
        result = []
        for i in nums:
            if i != 0:
                result.append(0 if count_zero > 0 else p_nozero // i)
            else:
                result.append(p_nozero if count_zero == 1 else 0)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends