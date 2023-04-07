# Depth First Search Approach

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Remove lands connected to edge
        def dfs(grid, i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                return
            if grid[i][j] == 0:
                return

            grid[i][j] = 0
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        for i in range(m):
            for j in range(n):
                if i * j == 0 or i == m - 1 or j == n - 1:
                    if grid[i][j] == 1:
                        dfs(grid, i, j)

        ans = 0

        for row in grid:
            ans += sum(row)

        return ans
