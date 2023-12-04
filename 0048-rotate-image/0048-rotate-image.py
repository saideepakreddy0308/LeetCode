class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # First (0,[1,2,3,4,5], then 1,[2,3,4,5], (0,1) -> (1,0), and then next row with (1,2) -> (2,1) so on ... )
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Reverse each row
        for row in matrix:
            row.reverse()