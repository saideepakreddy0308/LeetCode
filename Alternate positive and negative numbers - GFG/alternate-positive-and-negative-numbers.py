#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        p_arr = []
        n_arr = []
        res_arr = []
        
        for i in range(n):
            if arr[i] >= 0:
                p_arr.append(arr[i])
            else:
                n_arr.append(arr[i])
        
        while p_arr and n_arr:
            res_arr.append(p_arr.pop(0))
            res_arr.append(n_arr.pop(0))
            
        # Append any remaining elements
        res_arr.extend(p_arr)
        res_arr.extend(n_arr)
        
        arr[::] = res_arr[::]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends