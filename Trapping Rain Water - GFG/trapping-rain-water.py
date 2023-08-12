
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        lwp = [0] * n
        rwp = [0] * n
        sum = 0
        
        lwp[0] = arr[0]
        for i in range(0,n-1):
            lwp[i] = max(arr[i],lwp[i-1]) 
        
        rwp[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            rwp[i] = max(arr[i],rwp[i+1])
        
        for i in range(1,n-1):
            sum += (min(lwp[i],rwp[i]) - arr[i])
        
        return sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends