# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    palin = True
    
    for i in range(n):
        if str(arr[i]) != str(arr[i])[::-1]:
            palin = False
    return 1 if palin else 0



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends