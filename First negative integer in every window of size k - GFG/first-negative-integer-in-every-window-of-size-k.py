#User function Template for python3
from collections import deque

def printFirstNegativeInteger(arr, n, k):
    negative_numbers = deque()
    result = []

    for i in range(n):

        # If negative, add its index to the queue
        if arr[i] < 0:
            negative_numbers.append(i)

        # Remove indices that are out of the current window
        while negative_numbers and negative_numbers[0] < i - k + 1:
            negative_numbers.popleft()

        # i >= k - 1 ensures that we have seen at least 'k' elements
        if i >= k - 1:
            # If the deque is not empty, there's a negative number
            if negative_numbers:
                result.append(arr[negative_numbers[0]])
            # Else, the window doesn't have a negative number
            else:
                result.append(0)

    return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends