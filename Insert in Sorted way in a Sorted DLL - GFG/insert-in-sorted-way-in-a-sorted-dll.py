#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

def sortedInsert(head, x):
    #code here
    
    new_node = Node(x)
    
    # Case when list is empty
    if head is None:
        return new_node
    
    # If node to be inserted at the beginning
    if x < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    
    # initialize temp to head
    temp = head
    
    # find the insertion point
    while temp.next is not None and x > temp.next.data:
        temp = temp.next
    
    # Insert new node
    new_node.next = temp.next
    new_node.prev = temp
    
    if temp.next is not None:
        temp.next.prev = new_node
    
    temp.next = new_node
    
    return head
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    pvs=None
    while head:
        print(head.data, end=' ')
        if head.prev !=pvs:
            print('prev pointer not connected')
        pvs = head
        head = head.next
        


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        dll.head=sortedInsert(dll.head, x)
        displayList(dll.head)
        print()




# } Driver Code Ends