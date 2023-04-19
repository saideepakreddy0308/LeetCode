class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        # Basic Idea:
        #     if dist[u] + w[u,v] < dist[v]
        #     dist[v] = dist[u] + w[u,v]
        
    # Asked Naive Approach
       
        # initialize all node distances as inf
        dist = [float('inf') for _ in range(V)]
        
        # set dist of starting index 0
        dist[S] = 0
        
        # Create a list to indicare if a node is visited or not
        vis = [False for _ in range(V)]
        
        # Iterate over all the nodes
        for _ in range(V):
            
            #set u = -1 to indicate a current starting node
            u = -1
            
            # iterate over all the nodes to check the status of the visit
            # This portion of the function is iterating over all nodes in the graph to find the next node to visit based on the current distances.
            # The variable x is used to iterate over all the nodes in the graph. The first condition in the if statement, not vis[x], checks whether the node has been visited already or not. If the node has already been visited, then it skips over it and moves on to the next node.
            # The second condition, (u == -1 or dist[x] < dist[u]), checks whether the current node being examined x has a shorter distance than the previous node u that was visited. If u is -1 (which it is initially) or dist[x] is smaller than dist[u], then it updates the current node u to be x.
            # So essentially, this portion of the code is selecting the node with the shortest distance that has not yet been visited.

            for x in range(V):
                            # now if the 'x' node is not visited yet or the distance we have currently for it is less than the distance to the start node then update the current node as the 'x'
                if not vis[x] and (u == -1 or dist[x] < dist[u]):
                    u = x
                    
                    
            # check if we have visited all the nodes or we haven't reached the node
            if dist[u] == float('inf'):
                break
            # set the currently running node as visited
            vis[u] = True
            
            # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance.
            for v,d in adj[u]:
                if dist[u] + d < dist[v]:
                    dist[v] = dist[u] + d
            # Understand here how it works
            # print("u",u,"dist",dist)
                # now at last return the list which contains the shortest path to each node from that given node            
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