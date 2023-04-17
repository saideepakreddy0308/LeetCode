#User function Template for python3

class MyQueue:
    
    def __init__(self):
        self.items = []
    
    #Function to push an element x in a queue.
    def push(self, x):
         
        #add code here
        self.items.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self):
         
         # add code here
        if not bool(self.items):
           return -1
        else:
            return self.items.pop(0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends