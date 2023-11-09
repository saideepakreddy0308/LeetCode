# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right   
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def max_height(node):
            if node is None:
                return 0
            
            left_height = max_height(node.left)
            right_height = max_height(node.right)
            
            # Calculate the diameter through the current node
            diameter_through_node = left_height + right_height
            
            # Update the maximum diameter found so far
            self.max_diameter = max(self.max_diameter, diameter_through_node)
            
            # Return the height of the current subtree
            return max(left_height, right_height) + 1

        self.max_diameter = 0
        max_height(root)
        return self.max_diameter
