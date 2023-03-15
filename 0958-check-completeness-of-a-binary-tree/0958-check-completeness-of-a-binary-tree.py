# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        is_null_in_between_nodes = False
        
        while queue:
            total_nodes_in_level = len(queue)
            for i in range(total_nodes_in_level):
                curr_node = queue.popleft()
                if curr_node is None:
                    is_null_in_between_nodes = True
                else:
                    if is_null_in_between_nodes:
                        return False
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
        return True

# Time Complexity: O(N) , we visit each node exactly once
# Space Complexity: O(N), Maximum number of nodes at any level. In worst case its last level, having N/2 nodes( in a complete binary tree). The size of the tree can go upto N/2.