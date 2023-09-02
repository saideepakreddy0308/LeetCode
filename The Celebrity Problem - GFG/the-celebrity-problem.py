#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        
        # Two pointer approach
        # One at beginning and one at end:
        left = 0
        right = n - 1
        
        while left < right:
            # if left knows right, left cannot be a celebrity
            if M[left][right] == 1:
                # moving to next person
                left += 1
            
            # if left doesnt know right, right cannot be the celebrity
            else:
               right -= 1
        
        # At this point , 'left' is a potential celebrity canditate
        # we really need to verify if he is indeed a canditate
        for i in range(n):
            # skip checking'left' with itself
            if i == left:
                continue
            # If 'left' knows anyone or someone doesn't know 'left', 'left' cannot be the celebrity
            if M[left][i] == 1 or M[i][left] == 0:
                return -1
                
        # Finally, if we reach here, 'left' is the celebrity
        return left

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends