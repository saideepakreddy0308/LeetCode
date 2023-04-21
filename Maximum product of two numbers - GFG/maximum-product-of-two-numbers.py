#User function Template for python3
class Solution:

	def maxProduct(self,arr, n):
		# code here
		# max1 -> highest max
		# max2 -> second highest max
		
		max1 = max2 = float('-inf')
    
        # loop through the array
        for num in arr:
            # if the current element is greater than or equal to the maximum element
            # update the maximum and second maximum element
            if num >= max1:
                max2 = max1
                max1 = num
            # if the current element is greater than the second maximum element
            # update the second maximum element
            elif num > max2:
                max2 = num
        
        # return the product of the two maximum elements
        return max1 * max2
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends