from collections import defaultdict , deque 

import heapq as hq

class Solution:

    def dijkstra(self, V, adj, S):

        dist=[float('inf')]*V

        dist[S]=0

        heap=[]

        hq.heappush(heap,(S,0))

        while heap:

            pnode,pdist=hq.heappop(heap)

            for i in adj[pnode]:

                cnode=i[0]

                cdist=i[1]

                if cdist+pdist< dist[cnode]:

                    dist[cnode]=cdist+pdist

                    hq.heappush(heap,(cnode,dist[cnode]))

        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends