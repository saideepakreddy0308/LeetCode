Check Submissions - Different Methods and Interesting Solutions.
​
class Solution:
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
m,n = len(image),len(image[0])
initial_color = image[sr][sc]
​
q = deque([[sr,sc]])
visited = set()
visited.add((sr,sc))
​
while q:
r,c = q.popleft()
image[r][c] = color
​
for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
row,col = r+dr,c+dc
if 0 <= row < m and 0 <= col < n and image[row][col] == initial_color and (row,col) not in visited:
q.append([row,col])
visited.add((row,col))
return image
2nd Approach:
class Solution:
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
​
start_color = image[sr][sc]
​
# recursive solution - dfs
​
def flood_fill(x,y):
if x < 0 or x >= len(image): return
if y < 0 or y >= len(image[0]): return
​
if image[x][y] == color: return
if image[x][y] != start_color: return
​
image[x][y] = color
​
flood_fill(x-1,y) # up
flood_fill(x+1,y) # down
flood_fill(x,y+1) # right
flood_fill(x,y-1) # left
​
flood_fill(sr,sc)
return image
​
3rd Approach (Much Interesting)