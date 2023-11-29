class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows,cols = len(matrix), len(matrix[0])
        left,right = 0, rows * cols - 1
        
        
        while left <= right:
            mid = (left + right) // 2
            mid_elt = matrix[mid//cols][mid % cols]  # int quotient, int remainder
            
            if mid_elt == target:
                return True
            elif mid_elt < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # T.C: O(log(M*N))
    # S.C: O(1)