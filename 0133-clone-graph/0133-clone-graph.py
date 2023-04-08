"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # Hashmap to check whether clone of nodes made, to avoid duplicates of same node
        oldToNew = {}
        
        
        # Depth First Search
        def dfs(node):   # def clone(node)
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))   # clone(nei)
            return copy
        
        return dfs(node) if node else None