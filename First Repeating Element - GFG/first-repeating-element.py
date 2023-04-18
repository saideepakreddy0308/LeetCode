#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        ht = {}
        # count = {}
        min_index = 1000000
        for (i,num) in enumerate(arr):
            if num not in ht:
                ht[num] = i + 1
            elif num in ht:
                min_index = min(min_index,ht[num])
        return min_index if len(ht) != n else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends