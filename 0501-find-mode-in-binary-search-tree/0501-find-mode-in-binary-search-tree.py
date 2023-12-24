# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        ht = {}
        
        def xyz(node):
            if node is None:
                return
            
            ht[node.val] = ht.get(node.val,0) + 1
            xyz(node.left)
            xyz(node.right)
        
        xyz(root)
        k = max(ht.values())
        
        return [ x for x in ht if ht[x] == k]