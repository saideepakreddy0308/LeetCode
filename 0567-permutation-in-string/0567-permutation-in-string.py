class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ht_s1 = {}
        ht_s2 = {}
        j = 0
        
        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            ht_s1[s1[i]] = ht_s1.get(s1[i], 0) + 1
        
        for i in range(len(s1)):
            ht_s2[s2[i]] = ht_s2.get(s2[i], 0) + 1
            
        for i in range(len(s1), len(s2)):
            if ht_s1 == ht_s2:
                return True
            else:
                ht_s2[s2[i]] = ht_s2.get(s2[i], 0) + 1
                ht_s2[s2[j]] -= 1
                if ht_s2[s2[j]] == 0:
                    del ht_s2[s2[j]]
                j += 1
                
        return ht_s1 == ht_s2             # <- at the end, to check the last one

# t.c: O(len(s2))
# s.c: O(min(len((s1,s2)))