class Solution:
    def partitionString(self, s: str) -> int:
        
        # Greedy Approach
        # Intuition:
        # 1. We consider adding characters to a sunstring as long as we see a character that has already been added to the current substring.
        # 2. When we see a character already present in substring, we start a new substring
        # 3. We repeat this process until we iterate over the entire string
        
        # To find way
        # We need to find minimum number of partitions i.e form larger substrings, resulting in lower total number of substrings formed
        
        # 1. Using array of size 26, to keep track characters of ongoing substring, by uploading index position to each
        # 2. Or Hashset to track only the characters
        # IMPORTANT POINT: We must clear it completely back to actual/neutral state at the start of each substring, if hashset
        
        lastSeen = [-1] * 26
        count = 1
        substringStarting = 0
        
        # Input: s = "abacaba"
        # Output: 4
        # Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").


        for i in range(len(s)):  #O(N)
            
            # Check if most recent positon is already included in the substring
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            # And also, we update the lastSeen for the current character by i   
            lastSeen[ord(s[i]) - ord('a')] = i
            
        return count
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)