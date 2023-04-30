#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        
        c = [] # alternate result array
        pos = []  # pos array
        neg = []  # neg array
        
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        
        n = min(len(pos), len(neg))
        
        for i in range(n):
            c.append(pos[i])
            c.append(neg[i])
        
        if len(pos) > n:
            c.extend(pos[n:])
        elif len(neg) > n:
            c.extend(neg[n:])
        
        
        arr[::] = c[::]
        del pos
        del neg
        
        return c

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