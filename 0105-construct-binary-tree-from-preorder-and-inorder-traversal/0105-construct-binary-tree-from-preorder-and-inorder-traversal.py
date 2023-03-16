# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        indx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:indx+1],inorder[:indx])
        root.right = self.buildTree(preorder[indx+1:],inorder[indx+1:])
        
        return root