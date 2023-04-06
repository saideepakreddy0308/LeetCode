class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        # Intuition:
            # To go through all the cells and check whether its neighbours are matching the condition i.e top,right, bottom, left are surrounded by 1. If so then its a closed island else move on.
            
        # Approach
            # 1. Firstly, loop through the rows and cols
            # 2. Maintain a SET. Why? Let's say we are on the cell (say c) and we searched its neightbours (say n number) for 1 or 0. Now in the future iterations we will be eventually going to iterate over n (because of our loops). So this will lead to iterate over (c) even though we have already checked that cell and will lead to unnecessary recursive calls. To avoid this we will mark that cell (c) as visited by adding it to the set.
            # 3. Create a DFS funtion which will only return 0 or 1. "O" if out of bounds and "1" if the cell = 1 or if we have visited it.
            # 4. If either of the above condition fails then that means it is a completely new cell and we can carry on the recursion.
            # 5.Finally return min of all 4 recursice calls. Why min? Because lets say in our first call row got out of bounds which means it will return 0 and we know if any row or col reaches its boundaries then we must return 0 so we just use min to calculate that.


        ROWS, COLS = len (grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r <0 or c <0 or
                r == ROWS or c == COLS):
                    return 0 # False
            if grid[r][c] == 1 or (r, c) in visit:
                return 1 # True
            visit.add((r, c))

            return min(dfs(r+1, c), dfs(r-1,c), dfs(r, c+1), dfs(r, c-1))
        
        res = 0
        for r in range (ROWS):
            for c in range (COLS):
                if not grid[r][c] and (r, c) not in visit:
                    res += dfs(r, c)
        return res
    
# Time Complexity: O(M*N)
# Space Complexity: O(1)