# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reverse(node):
            if not node:
                return
            node.left,node.right = node.right, node.left
            reverse(node.left)
            reverse(node.right)
            return root
        
        return reverse(root)  #asked to return its root
    # t.c: O(n/2), O(n)
    # s.c: O(h), height of tree