class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        sign = '+'
        
        for i, char in enumerate(s):
            
            if char.isdigit():
                num = num * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                num = 0
                sign = char

        return sum(stack)
    
    # T.C: O(n), single pass thorough the string
    # S.C: O(n), stack_size proportional to lwngth of string