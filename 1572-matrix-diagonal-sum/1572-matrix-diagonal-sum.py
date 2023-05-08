class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total = 0
        n = len(mat[0])-1
        
        for i in range(len(mat)):
		    # Add primary diagonal.
            total += mat[i][i]
			# Add the secondary but avoid the middle point that overlaps the primary.
            if i != n-i:
                total += mat[i][n-i]
            
        return total