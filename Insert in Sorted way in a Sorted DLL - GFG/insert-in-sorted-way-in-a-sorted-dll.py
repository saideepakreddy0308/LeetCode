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
    
    if head is None:  # If head is none
        head = new_node
        return new_node
    
    if head.data > x:  # If x to be inserted at position 1 , at first(head)
        new_node.next = head
        head.prev = new_node
        return new_node
        
    temp = head
    while temp.next != None:
        if temp.next.data > x:  # Find the position where we need to insert x
            break
        temp = temp.next
        
    # If position found, insert the element
    new_node.next = temp.next
    if temp.next:  # At last element
        temp.next.prev = new_node   # As nonetype object does not have attribute "prev"
    temp.next = new_node
    new_node.prev = temp
    
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