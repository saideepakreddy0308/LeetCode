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
        
        # Alt + F3 = select all occurences of a selection
        
        e=""
        c=0
        for i in s:
            if i not in e:
                e+=i
            else:
                e=""
                c+=1
                e+=i
        return c+1

    
    # Time Complexity: O(N)
    # Space Complexity: O(k), where k is size of the string s, to track unique characters
    # The maximum size can be size of entire string