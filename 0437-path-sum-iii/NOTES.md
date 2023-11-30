### Definition for a binary tree node.
# class TreeNode:
class Solution:
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
# DFS to traverse, maintain running_sum to keep track the sum of values along current_path ( prefix sums)
# dict to store the count of prefix_sum encountered so far , key,value be prefix_sum, count_of_paths
# for each node, check if there is prefix sum in dict, add count to result
# update with current prefix sum, recursive calls for left and right subtrees
# Backtrack, remove curr_sum from dict
# return, total_count_of_paths
​
if not root:
return 0
​
# Helper function to traverse the tree and count paths
def dfs(node, current_sum, path_sums):
if not node:
return 0
​
current_sum += node.val
count = path_sums.get(current_sum - targetSum, 0)
path_sums[current_sum] = path_sums.get(current_sum, 0) + 1
​
# Recursive calls for left and right subtrees
count += dfs(node.left, current_sum, path_sums)