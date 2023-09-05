#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    
	   # If there's only one element, you are already at the end
	   if n <= 1:
	       return 0
	   
	   # If the first element is zero, you can't make any jump
	   if arr[0] == 0:
	       return -1
	   
	   # Variables initiate
	   
	   # maxReach, it stores the farthest index we can reach from the current posiiton
	   maxReach = arr[0]  # 1
	   
	   # steps stores the number of steps we can still take
	   steps = arr[0]  # 1
	   
	   # jumps stores the number of jumps we've taken so far
	   jumps = 1  # we need atleast one jump
	   
	   # Starting from index 1 as we have already considered index 0
	   for i in range(1,n):
	       
	       # if we reach at end of the array, return the number of jumps:
	       if i == n - 1:
	           return jumps
	       
	       #Update maxReach if a farthest index can be reached from this position
	       maxReach = max(maxReach, i + arr[i])        # max(1,1 + 3) = 4
	        
	       #Decrease the number of remaining steps
	       steps -= 1                       # after first iteration ->  step = 0
	       
	       # If no steps are remaining
	       if steps == 0:           # so now at index 1 as eligible steps from position 0 ended.
	           #Increment the number of jumps.
	           jumps += 1           # increase for second jump to be done, as we havent reached.
	           
	           # If we can't move any further, return -1
	           if i >= maxReach:    # at the psotion where i = 0 and maxReach is <= i: mostly happen when 0 is the final maxreach.
	               return -1
	               
	           # Update steps to the number of steps needed to reach the maxReach
	           steps = maxReach - i
	       
	   # If the end of the array isn't reachabke , return -1
	   return -1
	           
	       


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends