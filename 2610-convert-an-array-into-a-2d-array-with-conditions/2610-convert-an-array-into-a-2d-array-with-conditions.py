class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1

        heap = []
        for key in memo:
            heappush(heap, (-memo[key], key))
        
        freq, num = heappop(heap)
        freq = -freq

        res = [[num] for  i in range(freq)]

        while heap:
            freq, num = heappop(heap)
            for i in range(-freq):
                res[i].append(num)
            
        return res