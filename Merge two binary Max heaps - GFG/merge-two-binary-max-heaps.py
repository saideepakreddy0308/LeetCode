#User function Template for python3

class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        arr = a + b
        N = n + m
        
        def heapify(arr,N,i):
            largest = i
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            
            if left_i < N and arr[left_i] > arr[largest]:
                largest = left_i
            if right_i < N and arr[right_i] > arr[largest]:
                largest = right_i
                
            if largest != i:
                arr[largest],arr[i] = arr[i],arr[largest]
                heapify(arr,N,largest)
        for i in range(N//2 - 1,-1,-1):
            heapify(arr,N,i)
            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends