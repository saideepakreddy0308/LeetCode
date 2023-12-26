# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_count = 0 
        prev = None
        count = 0
        res = []
        def dfs(node):
            nonlocal prev , max_count,count, res
            if not node:
                return None
                
            dfs(node.left)
            if not prev:
                count = 1
            elif prev and prev.val == node.val:
                count += 1
            else:
                count = 1
            prev = node

            if count == max_count:
                res.append(node.val)
            elif count > max_count:
                max_count = count
                res = [node.val]

            dfs(node.right)
        dfs(root)
        return res