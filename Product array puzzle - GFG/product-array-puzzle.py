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
        
        # replacing elements in nums by productexpectself
        # Case1: if there is no "0" in nums"
        if count0==0:
            for i in range(n):
                nums[i]=mul//nums[i]
        # Case2: if there is "0" in nums"
        elif count0==1:
            for i in range(n):
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=mul
        # Case3: if 2 or more "0"'s present
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