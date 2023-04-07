class Solution:
    def partitionString(self, s: str) -> int:
        # Hash Set approach
        e = ''
        count = 0
        for i in s:
            if i in e:
                count += 1
                e = ' '
                e += i
                    
            e += i
        return count + 1
        