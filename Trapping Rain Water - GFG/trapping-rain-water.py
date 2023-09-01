
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        
        sum = 0
        
        # Left_Wall_Heights
        l_side = [0] * n
        l_side[0] = arr[0]
        for i in range(1,n):
            l_side[i] = max(l_side[i-1],arr[i])
        
        # Right_wall_Heights\
        r_side = [0] * n
        r_side[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            r_side[i]= max(r_side[i+1],arr[i])
        
        
        for i in range(1,n-1):
            sum += (  min(l_side[i],r_side[i]) - arr[i] )
        
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