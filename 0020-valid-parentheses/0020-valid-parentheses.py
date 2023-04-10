class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        stack = []
        
        for c in s:
            if c not in mapping:
                if not stack or mapping[stack.pop()] != c:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0