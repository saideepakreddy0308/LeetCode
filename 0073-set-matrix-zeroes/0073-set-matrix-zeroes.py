class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        
        # containing zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # zeros to identified rows
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0
        
        # zeros to identified cols
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
        
        # T.C: O(m*n), S.C: O(M+N), two_sets