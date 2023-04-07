class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Depth First Search
        
        # 0 -> Land
        # 1 -> Water
        # Find Number of Closed Lands
        
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        
        def dfs(r,c):
            # If its open island
            if (r < 0 or c < 0 or c == COLS or r == ROWS):
                return 0 # False
            if grid[r][c] == 1 or (r,c) in visit:
                return 1 # True
            # Now,Hash set to mark if its a ( Not visited grid[r][c] of 0, to avoid recursions)
            visit.add((r,c))
            
            return min(dfs(r+1,c),dfs(r-1,c),dfs(r,c+1),dfs(r,c-1))
        
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                # If its land and visited, we dont want to do recursion again, we take only if not visited
                if not grid[r][c] and (r,c) not in visit:
                    result += dfs(r,c)
        return result
    # T.C: O(M*N)
    # S.C: O(M*N)