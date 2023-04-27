#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        mul=1
        count0=0
        for i in nums:
            if i!=0:
                mul*=i
            else:
                count0+=1
        if count0==0:
            for i in range(n):
                nums[i]=mul//nums[i]
        elif count0==1:
            for i in range(n):
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=mul
        else:
            for i in range(n):
                nums[i]=0
        return nums

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