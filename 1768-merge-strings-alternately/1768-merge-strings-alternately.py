class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Two Pointers Approach
        l1 = len(word1)
        l2 = len(word2)
        
        i = 0
        j = 0
        
        result = []
        
        while i < l1 or j < l2:
            if i < l1:
                result += word1[i]
                i += 1
            if j < l2:
                result += word2[j]
                j += 1
        
        return "".join(result)