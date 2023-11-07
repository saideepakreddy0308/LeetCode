class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def char_count_of(s):
            char_count = {}
            for x in s:
                char_count[x] = char_count.get(x,0) + 1
            return char_count
        
        if char_count_of(s) == char_count_of(t):
            return True
        else:
            return False