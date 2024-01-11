class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, family, diff):
            family.append(node.val) # family is a list of nodes belong to a path, keep appending as searching occurs
            
            if node.left is not None: # Search on the left if it exists
                diff = dfs(node.left, family, diff)
            if node.right is not None: # Search on the right if it exists
                diff = dfs(node.right, family, diff)

            if node.left is None and node.right is None: # When reaches dead end of a path
                diff = max(diff, max(family) - min(family)) # Find max, min of a path; subtract to get the difference -> get max between previous diff & current diff
            
            family.pop() # Remove the current node until we can move on to next path
            return diff

        return dfs(root, [], 0)