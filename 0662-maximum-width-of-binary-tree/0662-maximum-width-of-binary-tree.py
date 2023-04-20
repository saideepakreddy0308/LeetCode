# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root_: TreeNode) -> int:
        def level_order_widths(root: TreeNode) -> Iterable[int]:
            level = ((0, root),)
            while level:
                yield level[-1][0] - level[0][0] + 1
                level = tuple(
                    (j, child)
                    for i, node in level
                    for j, child in enumerate((node.left, node.right), 2 * i)
                    if child
                )
        
        return max(level_order_widths(root_))

# T.C: O(N)
# S.C: O(N)