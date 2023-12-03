class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        n = len(T)
        res = [0] * n
        
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if T[j] > T[i]:
#                     res[i] = j - i
#                     break
#         return res

# Stack
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        
        return res