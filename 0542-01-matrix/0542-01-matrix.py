from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        if not mat:
            return mat
        
        rows, cols = len(mat), len(mat[0])
        
        # queue for BFS
        queue = deque()
        
        # Add all '0' cells to the queue and mark them as visited
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                else:
                    mat[i][j] = float('inf') # Mark '1' cells with infinity
        
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        # up,down,left,right
        
        while queue:
            i, j, distance = queue.popleft()
            
            for di,dj in directions:
                ni,nj = i + di, j + dj
                
                
                # Check if new position is within bounds
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] > distance + 1:
                    mat[ni][nj] = distance + 1
                    queue.append((ni,nj,distance+1))
        return mat
    
# T.C: O(rows * cols), every cell is visited once during the BFS process
# S.C: O(rows * cols), due to queue used for BFS, in worst casae, the queue may store all cells