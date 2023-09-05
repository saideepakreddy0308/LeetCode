#User function template for Python 3

from collections import Counter

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        counter = Counter(A)
        majority_count = N // 2
    
        for num, count in counter.items():
            if count > majority_count:
                return num
    
        return -1

# class Solution:

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends