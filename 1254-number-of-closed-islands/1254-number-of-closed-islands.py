class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            
            # If its open island
            if (r < 0 or c < 0 or r == ROWS or c == COLS):
                return 0  # False
            # If water, we need not to run DFS and also if visited
            if grid[r][c] == 1 or (r,c) in visit:  
                return 1 # True, this is a closed island, as far as concerned
            # Hashset, mark the land tile visited, to avoid infinite recursions
            visit.add((r,c))
            
            return min(dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r,c-1))
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                # if its land and not visited, we dont want to do recursion on it again.
                if not grid[r][c] and (r,c) not in visit:
                    result += dfs(r,c)
        return result   

# Time Complexity: O(M*N)
# Space Complexity: O(M*N), worst case scenerio