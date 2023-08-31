#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        
        x = n // k
        result = 0
        
        ht = {}
        for i in arr:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        for i in ht.values():
            if i > x:
                result += 1
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends