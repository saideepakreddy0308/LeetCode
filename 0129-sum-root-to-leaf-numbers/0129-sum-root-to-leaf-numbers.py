# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,s):
            if not node.left and not node.right:
                return int(s)
            total = 0
            if node.left:
                 total += dfs(node.left,s+ str(node.left.val))
            if node.right:
                total += dfs(node.right,s+ str(node.right.val))
            return total
        return dfs(root,str(root.val))