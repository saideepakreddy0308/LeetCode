class Solution:
    def removeStars(self, s: str) -> str:
        i=0
        out=""
        while(i<len(s)):
            if s[i]=="*":
                out=out[:-1]
            else:
                out=out+s[i]
            i+=1
        return out

# T.C : O(N)
# S.C : O(N)