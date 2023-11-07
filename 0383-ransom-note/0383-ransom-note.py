class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ht_r = {}
        ht_m = {}
        
        def char_count(st):
            ht = {}
            for s in st:
                ht[s] = ht.get(s,0) + 1
            return ht
        
        ht_r = char_count(ransomNote)
        ht_m = char_count(magazine)
        
        for k in ht_r:
            if k not in ht_m or ht_r[k] > ht_m[k]:
                return False 
        return True