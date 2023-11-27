**Idea:** To build a graph, where each mail is a node, and if two emails are connected, they represent the same person. After building DFS, or BGS to group together connected emails.
​
Certainly! Let's walk through the process with the given example:
​
```python
accounts = [
["John", "johnsmith@mail.com", "john00@mail.com"],
["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"],
["Mary", "mary@mail.com"]
]
```
​
### Step 1: Build the Graph
​
Build a graph where each email is a node, and connected emails represent the same person. Use a defaultdict to store email connections.
​
Graph:
```
{
'johnsmith@mail.com': ['john00@mail.com', 'john_newyork@mail.com'],
'john00@mail.com': ['johnsmith@mail.com'],
'johnnybravo@mail.com': [],
'john_newyork@mail.com': ['johnsmith@mail.com'],
'mary@mail.com': []
}
```
​
### Step 2: DFS Traversal
​
Perform DFS traversal to group together connected emails.
​
1. **Start with "johnsmith@mail.com":**
- Visit "johnsmith@mail.com" and add it to the group.
- DFS to "john00@mail.com" and "john_newyork@mail.com".
​
2. **DFS from "john00@mail.com":**
- Visit "john00@mail.com" and add it to the group.
- DFS to "johnsmith@mail.com" (already visited).
​
3. **DFS from "john_newyork@mail.com":**