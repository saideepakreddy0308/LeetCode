from collections import deque

# Breadth First Search Approach
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        # Initialize variables
        count = 0
        r,c = len(grid), len(grid[0])
        
        q = deque()
        visited = [[False for _ in range(c)] for _ in range(r)]
        
        # Check all cells in the grid
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and not visited[i][j]:
                    closed = True
                    q.append((i, j))
                    visited[i][j] = True
                    
                    # BFS to check if the island is closed
                    while q:
                        x,y = q.popleft()
                        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                            nx,ny = x + dx, y+dy
                            
                            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                                closed = False
                            elif grid[nx][ny] == 0 and not visited[nx][ny]:
                                q.append((nx,ny))
                                visited[nx][ny] = True
                    # Increase count if island is closed
                    if closed:
                        count += 1
        return count
                
        