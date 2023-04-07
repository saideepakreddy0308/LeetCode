class Solution:
    def partitionString(self, s: str) -> int:
        # Hash Set approach
#         e = ''
#         count = 0
#         for i in s:
#             if i in e:
#                 count += 1
#                 e = ' '
#                 e += i
                    
#             e += i
#         return count + 1
    
        # Greedy Approach 
        lastSeen = [-1] * 26
        count = 1
        substringStarting = 0
        
        for i in range(len(s)):
            if lastSeen[ord(s[i])-ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
    
            lastSeen[ord(s[i])-ord('a')] = i
        
        return count
    
        