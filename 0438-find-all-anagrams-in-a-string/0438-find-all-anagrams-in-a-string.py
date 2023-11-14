import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        l_s = len(s)
        l_p = len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[:l_p])
        
        for i in range(l_s - l_p + 1):
            if counter_s == counter_p:
                result.append(i)
            
            if i + l_p < l_s:
                # removing outgoing and adding incoming character
                counter_s[s[i]] -= 1
                if counter_s[s[i]] == 0:
                    del counter_s[s[i]]
                counter_s[s[i+l_p]] += 1
        return result
            