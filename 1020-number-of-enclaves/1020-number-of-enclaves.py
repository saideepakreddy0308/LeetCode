# Breadth First Search Approach
import collections

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        ROWS,COLS = len(grid),len(grid[0])
        ans = 0
        
        # Idea is to put only the boundary 1's into queue and eliminate all the neighbour 1's of those and itself, and then get the grid with the remaining 1's
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    q.append((r,c))
        dir = [[-1,0],[0,1],[1,0],[0,-1]]
        
        while q:
            
            r,c = q.popleft()
            grid[r][c] = 0
            for dr,dc in dir:
                R = r + dr
                C = c + dc
                
                if (R >= 0 and R < ROWS and C >= 0 and C < COLS and grid[R][C] == 1):
                    grid[R][C] = 0
                    q.append((R,C))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans += 1
        return ans