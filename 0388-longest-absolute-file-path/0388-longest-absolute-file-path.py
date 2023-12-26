class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        lines = input.split('\n')
        stack = []
        max_len = 0
        
        
        for line in lines:
            tabs = line.count('\t')
            print("line = ", line, "\t in no. =",tabs)
            
            print("len of stack", len(stack))
            while len(stack) > tabs:
                print(stack[-1], "is popped")
                stack.pop()
            
            name = line.replace(
        '\t','')
            if '.' in name: # Its a file
                current_len = sum(len(part) + 1 for part in stack) + len(name)
                max_len = max(max_len, current_len)
            else: # Its a dictionaty
                stack.append(name)
                print("stack is appended with", name)
            
        
        return max_len
    