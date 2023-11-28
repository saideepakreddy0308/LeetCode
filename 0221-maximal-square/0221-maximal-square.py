class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        
        # 2D array to store the side length of largest square ending at each position
        dp = [[0] * cols for _ in range(rows)]
        
        max_side = 0 # variable to track the maximum side length
        
        for i in range(rows):
            for j in range(cols):
                
                if matrix[i][j] == '1':
                    # Calculate the side length of sqaure ending at this position
                    # If the current position is in the first row or first column, and we handle it separately.
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                
                max_side = max(max_side, dp[i][j])
        
        return max_side * max_side
    
    # O(M*N), both t.c and s.c