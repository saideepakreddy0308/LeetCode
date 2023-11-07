class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        ht = {}
        res = 0
        count = 0

        for x in s:
            ht[x] = ht.get(x, 0) + 1

        for i in ht.values():
            res += 2 * (i // 2)
            if i % 2 != 0:
                count = 1

        return res + count
