# https://www.youtube.com/watch?v=XgP3w7Txvlc
from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(set)
        for i, num in enumerate(arr):
            graph[num].add(i)

        queue = deque([(0, 0)]) # (now_index, steps)
        vis = set([0])
        while queue:
            now,steps = queue.popleft()
            if now == len(arr) - 1:
                return steps
            if (now + 1) not in vis and (now + 1) < len(arr):
                vis.add(now + 1)
                queue.append((now + 1, steps + 1))
            if (now - 1) not in vis and (now - 1) >= 0:
                vis.add(now - 1)
                queue.append((now - 1, steps + 1))
            for jump in graph[arr[now]]:
                if jump not in vis:
                    vis.add(jump)
                    queue.append((jump, steps + 1))
            del graph[arr[now]]