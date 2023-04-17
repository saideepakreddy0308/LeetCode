#User function Template for python3

def push(arr,n): 
    
    #return a queue with all elements of arr inserted in it
    return list(arr)
    # return arr
    
    
def _pop(q):
    
    #dequeue elements and print them
    while q:
        x = q.pop(0)
        print(x, end = ' ')

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arr = list(map(int,input().strip().split()))
        q=deque()
        q=push(arr,n)
        _pop(q)
        print()
# } Driver Code Ends