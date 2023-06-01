class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Idea:
        # search for the shortest path from start point to end point through BFS
        
        # Approach
        # Use queue to store the grids to be processed. Intially adds the starting point to the queue and each time take out a grid for processing,
        # explore its adjacent grids, and add unvisited grids to the queue. This process continues until an end point is found empty or the queue is empty.
        
        n = len(grid)
        
        # Check is start/end cell is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # Create queue for BFS and enqueue the first cell
        queue = deque([(0,0,1)])   #(row,col,path_length)
        
        # Offset in 8 directions
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
        
        #Execute BFS
        
        while queue:
            row,col,path_len = queue.popleft()
            
            #Check if the goal is reached
            if row == n-1 and col == n-1:
                return path_len
            
            # Explore adjacent grids:
            for i,j in directions:
                neighbor_row = row + i
                neighbor_col = col + j
                
                # Check if the adjacent grid is not visited and it is within the grid range
                if 0 <= neighbor_row < n and 0 <= neighbor_col < n and grid[neighbor_row][neighbor_col] == 0:
                    # Mark the adjacent cells as visited (set to 1)
                    grid[neighbor_row][neighbor_col] = 1
                    queue.append((neighbor_row,neighbor_col,path_len + 1))
        
        # If no clear path found
        return -1
            
                
        
        