# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.pathLength = 0
        
        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                # Currently, visited right child, go for left child, increase steps and goLeft further as False
                if goLeft:
                    dfs(node.left, False,steps + 1)
                    dfs(node.right,True,1)
                # Currently, visited left child, go for right child, increase steps and goLeft further as True
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
           
        dfs(root,False,0)
        dfs(root,True,0)
        return self.pathLength
    
    # Time Complexity: O(N) , as we recursively visit both the children of each node once. O(N), and iterate over (n-1) egdes 
    # Space Complexity: O(N), recursion stack in worst case can have no more than n elements.
    
   

    # Intuition:
        # 1. If p node is left child & having l as left child, we cannot take the edge, do not form zigzag path
        # 2. We can form new zig zag path including edge between p and l, with length 1
        
        # 3. Similarly, if p is left child and r is right child, form zigzag path, opposite directions
        # 4. Increase the path length by 1
        
        # 5. Vice versa if p is right child and l,r considered for it.
        
        # We need to keep track the way we should consider forming a zig zag path
        # Consider DFS to traverse the tree, use of recursive function
        
    # Coding:
        # 1. Consider pathLength answer variable
        # 2. Boolean goLeft to indicate left for the continuation of the zigzag path
        # 3. steps variable to store the length of zigzag path so far
        
        # It's worth noting, we can substitute any indication for goLeft
        # We can use whether the parent node is left or right child, or we can choose whether to continue the zigzag path to the right(similar to the left)
        
        # we first determine whether the node is null or not.
        # If valid node, we update answer variable to max(pathLength,steps)
        
        # Process:
            # 1. If goLeft is true, the zigzag path will continue left side
            # 2. We cant go left in the next step to continue zigzag path, because we already going left in this step
            # 3. As a result we pass, dfs(node.left, false, steps + 1), we keep going a zigzag pattern
        
            # 4. Similarly, if we are in right child, next we need to visit left child the next time,  dfs(node.left, false,steps+1) &  dfs(node.right, true, 1)
            # 5. If we visited left child currently, for next time, dfs(node.right, True,steps+1) we keep continuing zig zag pattern