class Solution:
    def duplicates(self, arr, n): 
        a = [0] * n
        for num in arr:
	    	a[num % n] += n
	    
	    res = []
    	for index in range(n):

    		if a[index]  // n > 1:
    			res.append(index)
    			
    	return res if res else [-1]
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends