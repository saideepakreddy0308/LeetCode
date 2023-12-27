class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap={}
        i=0
        j=0
        res=0

        while j<len(s):
            hashMap[s[j]]=1+hashMap.get(s[j],0)

            while (j-i+1)-max(hashMap.values())>k:
                hashMap[s[i]]-=1
                i+=1

            res=max(res,j-i+1)
            j+=1
        
        return res
            