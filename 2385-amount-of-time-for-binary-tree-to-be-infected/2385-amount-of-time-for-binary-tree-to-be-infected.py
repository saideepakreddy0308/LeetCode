# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.min = [0]
        self.start = start
        self.first = root.val

        self.recursion(root)
        return max(self.min)

    def recursion(self, root):
        if not root:
            return [-1, 0]
        
        left, infection_l = self.recursion(root.left)
        right, infection_r = self.recursion(root.right)
        left += 1 
        right += 1

        if root.val == self.start:
            self.min.append(max(left,right))
            return [0,1]
        
        if infection_l:
            self.min.append(left+right)
            return [left,1]
        if infection_r:
            self.min.append(left+right)
            return [right,1]
        
        return [max(left,right),0]
