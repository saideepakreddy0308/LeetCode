# Iterative Dynamic Programming

# Intuition:
# 1. Generate all possible subsequences, and use recursion
# 2. If the first and last characters are the same, both characeters are guarenteed to be considered a final palindrome
# 3. We add 2 to answer variable and recursively remove first and last characters from remaining substring
# 4. Else, if first and last arent the same, we recurse over substring, 1. removing the first, 2. removing the second
# 5. we want maximum, we pick the maximum of both of these

# we can use bottom-up approach to solve problems without using recursion. We build answers to subproblems first, then use them to build answers to larger problems.

# Building from smaller to larger strings: We can begin by selecting all possible substrings of length '1', then find the largest palindromic subsequence in all substrings of length '2', then in length '3', and so on to obtain the answer for the entire string.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        # 2D array DP having n rows, n columns, where dp[i][j] contains longest p subsequence from index i to j in s
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,n):
                # print("i:"," ", i,"j:"," ",j)
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
                
        
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)