# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        # Build graph using adjacency list
        graph = defaultdict(list)
        self.buildGraph(root,None,graph)
        
        # Perform BFS starting from the target node to find node at distance
        queue = [(target, 0)]
        visited = set([target])
        result = []
        
        while queue:
            node, distance = queue.pop()
            
            if distance == k:
                result.append(node.val)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,distance + 1))

        return result
        
    def buildGraph(self,node,parent,graph):
        if node:
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
                
            self.buildGraph(node.left,node,graph)
            self.buildGraph(node.right,node,graph)
    
    # T.C: O(N), traversing node once when building graph, bfs also visits once
    # S.C: O(N), due to adjacency lsit, Bfs o< max no.of nodes at a single level, N/2 max, additional for visited set and result list