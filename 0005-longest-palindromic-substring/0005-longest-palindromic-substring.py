class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Brute Force
        def is_palindrome(s):
            return s == s[::-1]
        
        n = len(s)
        max_length = 0
        start = 0
        
        for i in range(n):
            for j in range(i+1,n+1):
                substring  = s[i:j]
                if is_palindrome(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    start = i
        
        return s[start:start+max_length]