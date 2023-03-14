# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using DFS Approach
# 1.we want sum all routes from root and return sum.
# 2.for this appropriate method would be dfs.
# 3.using dfs traverse till end of tree ie. leaf node.
# 4.keep track of path from root till leaf-node, now when encountered leaf node, sum it in answer.
# 5.do this till all path covered, return answer.

# A non-local variable is a variable used when there are nested functions, and we don’t want the variable of the inside function to be local within that function.

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(curr=None,path=''):
            nonlocal ans
            if curr:
                path += str(curr.val)
                dfs(curr.left,path)
                dfs(curr.right,path)
                if curr.left == None and curr.right == None:ans += int(path)
            return
        dfs(root)
        return ans        

# Time complexity: O(N)
# Space complexity: O(N)