# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Keep track of the topmost level in which there is a missing node
        missing = math.inf
        # Keep track of the tree's depth
        depth = 0
        # Use a stack for DFS
        stack = [(root,0)]

        # While the stack is populated
        while stack:
            # Get the next node in the DFS
            node, level = stack.pop()

            # If this node is None
            if not node:
                if level > missing:
                    return False
                # Update the topmost level in which we have seen a missing node
                missing = level
                # Go to the next node in DFS
                continue

            # If we have already encountered a missing node in this level and now have a
            # node in this level, the tree is not complete!
            if level == missing:
                return False

            # Move to the next level in the tree
            level += 1
            # Update the depth of the tree
            depth = max(depth, level)

            # Add the children – it is important to add the right first so that the 
            # left child is traversed first in our DFS!
            stack.append((node.right, level))
            stack.append((node.left, level))

        # Return True if the missing nodes are all either right below the tree
        # or in the last level of the tree
        return depth - missing <= 1