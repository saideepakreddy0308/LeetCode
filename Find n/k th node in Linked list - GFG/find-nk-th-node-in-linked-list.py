#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        

def fractionalNodes(head,k):
        #add code here
        temp = head
        l = 0
        while temp:
            l += 1  # length
            temp = temp.next
        
        x = (l + k - 1) // k
        
        temp1 = head
        for i in range(x-1):
            temp1 = temp1.next
        return temp1
            
                          


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 

# Linked List class
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
    
                    
    def display(self,node):
        while(node is not None):
            print(node.data,end=" ")
            node=node.next
            
            
            
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k=int(input())
        #head = createList(arr, n)
        for i in range(0,len(arr)):
            lis.insert(arr[i])
        ans=fractionalNodes(lis.head,k)
        print(ans.data)
# } Driver Code Ends