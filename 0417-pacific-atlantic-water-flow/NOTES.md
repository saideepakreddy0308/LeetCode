The very first time: Totally pending ... didnt understand the logic.
​
See youtube and learn if needed.
​
​
​
The line `visited[r][c] |= ocean` uses the `|=` operator, which is a shorthand for the bitwise OR assignment operator.
​
Here's what it does:
​
1. `visited[r][c]` is the value at the cell `(r, c)` in the `visited` array.
2. `ocean` is a value representing the ocean (either 1 for Pacific or 2 for Atlantic).
​
The `|=` operator performs a bitwise OR between the current value of `visited[r][c]` and `ocean`, and then assigns the result back to `visited[r][c]`. In simple terms, it's a way to set certain bits in `visited[r][c]` based on the value of `ocean`.
​
Here's a breakdown:
​
- If `visited[r][c]` is 0 and `ocean` is 1, `visited[r][c] |= ocean` will set the first bit to 1.
- If `visited[r][c]` is 0 and `ocean` is 2, `visited[r][c] |= ocean` will set the second bit to 1.
- If `visited[r][c]` is already 1 and `ocean` is 1, `visited[r][c] |= ocean` will keep the first bit as 1.
- If `visited[r][c]` is already 2 and `ocean` is 2, `visited[r][c] |= ocean` will keep the second bit as 1.
- If `visited[r][c]` is 3 (binary 11) and `ocean` is 1, `visited[r][c] |= ocean` will keep both bits as 1.
​
In the context of the code, this line is used to mark the cell `(r, c)` as reachable from either the Pacific or Atlantic Ocean, or both, depending on the value of `ocean`.
​
It's a concise way of updating the `visited` array based on the ocean we are exploring during the Depth-First Search (DFS).