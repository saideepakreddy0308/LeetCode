# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanceHelper(node):
            if node is None:
                return [True,0]  # indicate, depth
            
            left_h = balanceHelper(node.left)
            right_h = balanceHelper(node.right)
            
            height = 0
            isbalanced = False
            if left_h[0] and right_h[0] and abs(left_h[1] - right_h[1]) <= 1:
                height = max(left_h[1],right_h[1]) + 1
                isbalanced =True
                
            return [isbalanced,height]
            
        return balanceHelper(root)[0]  # we need to return, balance Helper too