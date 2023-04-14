# Recursive Dynamic Programming

# Intuition:
# 1. Generate all possible subsequences, and use recursion
# 2. If the first and last characters are the same, both characeters are guarenteed to be considered a final palindrome
# 3. We add 2 to answer variable and recursively remove first and last characters from remaining substring
# 4. Else, if first and last arent the same, we recurse over substring, 1. removing the first, 2. removing the second
# 5. we want maximum, we pick the maximum of both of these

# Using Two Pointers

# Use memoization, to avoid encountering the same problem again 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        
        memo = {}  # Assume it as 2D array
        
        def lps(l,r):
            
            if (l,r) in memo:
                return memo[(l,r)]
            if l > r:
                return 0
            if l == r:
                return 1
            
            if s[l] == s[r]:
                memo[(l,r)] = lps(l+1,r-1) + 2
            else:
                memo[(l,r)] = max(lps(l,r-1),lps(l+1,r))
            return memo[(l,r)]
        return lps(0, n-1)
    
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)