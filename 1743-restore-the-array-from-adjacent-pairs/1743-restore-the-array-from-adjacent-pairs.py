from collections import defaultdict, deque

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        
        # Find the start node ( degree 1, it can be start or end)
        start_node = None
        for node in graph:
            if len(graph[node]) == 1:
                start_node = node
                break
        
        # Reconstruct the array using DFS or BFS
        result = []
        visited = set()
        
        def dfs(node):
            visited.add(node)
            result.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        dfs(start_node)
        return result
    
    # T.C: O(N), using dfs O(N+E), here e can be upto 2n, but not sure. , S.C: O(N)