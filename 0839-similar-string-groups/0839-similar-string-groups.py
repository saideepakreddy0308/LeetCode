class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = self.createGraph(strs, n) # Create an adjacency list to represent the graph
        vis = [False] * n # Create a boolean array to keep track of visited nodes
        ans = 0
        for i in range(n):
            if not vis[i]: # Traverse the graph using BFS and count the number of connected components
                self.bfs(i, vis, adj)
                ans += 1
        return ans

    def bfs(self, i: int, vis: List[bool], adj: List[List[int]]) -> None: # Breadth-first search to traverse the graph
        q = deque()
        q.append(i)
        vis[i] = True
        while q:
            t = q.popleft()
            for j in adj[t]:
                if not vis[j]:
                    vis[j] = True
                    q.append(j)

    def createGraph(self, strs: List[str], n: int) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]): # Check if two strings are similar with max of 1 swap
                    ans[i].append(j)
                    ans[j].append(i)
        return ans

    def isSimilar(self, a: str, b: str) -> bool:
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c += 1
        return c == 0 or c == 2