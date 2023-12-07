class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: 
        
        m = len(image)
        n = len(image[0])
        
        initial_color = image[sr][sc]
        
        # BFS 
        q = deque([(sr,sc)])
        visited = set()
        visited.add((sr,sc))
        
        while q:
            r,c = q.popleft()
            image[r][c] = color
            
            # directions = []
            for dr,dc in [[-1,-0],[1,0],[0,1],[0,-1]]:
                row,col = r + dr, c + dc
                if 0 <= row < m and 0 <= col < n and ( image[row][col] == initial_color) and ((row,col) not in visited):
                    q.append((row,col))
                    visited.add((row,col))
        
        return image