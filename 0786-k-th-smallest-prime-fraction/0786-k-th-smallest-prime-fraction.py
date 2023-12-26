class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        pq = []
        
        for i in range(n-1):
            heapq.heappush(pq,( arr[i]/arr[-1],i,n-1)) 
            
        while k - 1:
            _,i,j = heapq.heappop(pq)
            if i < j - 1:
                heapq.heappush(pq, (arr[i]/ arr[j-1],i,j-1))
            
            k -= 1
        
        return arr[pq[0][1]], arr[pq[0][2]]