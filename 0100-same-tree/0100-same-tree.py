# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p_node, q_node):
            
            # case 0_1
            if p_node is None and q_node is None:
                return True
            # case 0_2
            if (p_node is None and q_node is not None) or (p_node is not None and q_node is None):
                return False
            # case 1
            elif p_node.val != q_node.val:
                return False
            # case 2
            elif helper(p_node.left,q_node.left) and helper(p_node.right,q_node.right):
                return True
            else:
                return False
            
        
        return helper(p,q)