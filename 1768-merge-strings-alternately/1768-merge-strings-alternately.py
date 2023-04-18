class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # One Pointer Approach
        l1 = len(word1)
        l2 = len(word2)
        
        n = max(l1,l2)
        
        result = []
        
        for i in range(n):
            if i < l1:
                result += word1[i]
            if i < l2:
                result += word2[i]
                
        return "".join(result)