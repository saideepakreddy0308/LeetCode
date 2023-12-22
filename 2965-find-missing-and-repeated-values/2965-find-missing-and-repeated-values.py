from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        x = n * n
        ans =  [0,0]
        total_sum = 0
        
        ht = defaultdict()
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in ht:
                    ht[grid[i][j]] = 1
                else:
                    ht[grid[i][j]] += 1 
                if ht[grid[i][j]] == 2:
                    ans[0] = grid[i][j]
                    
                total_sum += grid[i][j]
                    
        whole_sum =  ( x * (x + 1) ) // 2
        b = abs( whole_sum - total_sum +  ans[0] )
        ans[1] = b
        
        print(whole_sum, total_sum)
        return ans