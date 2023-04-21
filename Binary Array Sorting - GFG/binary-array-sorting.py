#User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        
        l = 0
        r = N - 1
        
        while ( l<= r):
            if(A[l] == 1 and A[r] == 0):
                A[l],A[r] = A[r],A[l]
                
                l += 1
                r -= 1
            
            if(A[l] == 0 and l <= N):
                l += 1
            if(A[r] == 1 and r >= 0):
                r -= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends