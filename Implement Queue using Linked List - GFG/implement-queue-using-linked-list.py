# A linked list (LL) node 
# to store a queue entry 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.front = None
        self.rear = None
    
    # def isEmpty(self):
    #     return self.front == None
    
    #Function to push an element into the queue.
    def push(self, item): 
        
        new_node = Node(item)
        #Add code here
        if not self.front:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
         
    
    #Function to pop front element from the queue.
    def pop(self):
         
        #add code here
        if self.front:
            popped_item = self.front
            self.front = self.front.next
            return popped_item.data
        else:
            return -1


#{ 
 # Driver Code Starts
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