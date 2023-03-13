# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Follow Up 
# 1. Recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)


    def helper(self, left, right):
        if not left or not right:
            return left == right

        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

# 2.Iterative
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root == None:
#             return True
#         stack1 = []
#         stack2 = []
#         stack1.append(root.left)
#         stack2.append(root.right)
        
#         while stack1 and stack2:
#             p = stack1.pop()
#             q = stack2.pop()
#             if (p==None and q!=None) or (q==None and p!=None) :
#                 return False
#             if p:
#                 if p.val != q.val:
#                     return False
#                 stack1.append(p.left)
#                 stack1.append(p.right)
#                 stack2.append(q.right)
#                 stack2.append(q.left)
                
#         return True