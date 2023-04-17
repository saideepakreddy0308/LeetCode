#User function Template for python3

#Function to reverse the queue.
def rev(q):
    #add code here
    # q is Queue Object
    # get() operation removes from the front of the Queue ;  enqueue()
    # put() operation adds the element back of the Queue; dequeue()
    # From the given queue, use a "STACK" to reverse the elements and append it back to queue
    if q.empty():
        return q

    stack = []
    while not q.empty():
        stack.append(q.get())

    while len(stack) > 0:
        q.put(stack.pop())

    return q

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends