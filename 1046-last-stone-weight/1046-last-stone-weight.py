class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap,-stone) #-8
        print(maxheap)

        while len(maxheap) > 1:
            st1 = heapq.heappop(maxheap) #  -8
            st2 = heapq.heappop(maxheap)  # -7
            if st1 != st2:
                heapq.heappush(maxheap,-(st2-st1))
            
            print(maxheap)
        return -(maxheap[0]) if len(maxheap) == 1 else 0    