class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_around_center(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
            
        
        
        n = len(s)
        start = 0
        max_length = 0
        
        for i in range(n):
            len1 = expand_around_center(s,i,i)  #bab
            len2 = expand_around_center(s,i,i+1)  #baab
            current_length = max(len1,len2)
            
            if current_length > max_length:
                max_length  = current_length
                # the start index of the current palindrome.
                start = i - (current_length - 1) // 2
        
        return s[start:start+max_length]
    
    # T.C: O(n^2) ; outerloop -> o(n) and def expand_around_funcion, in worstcase may run up to O(n), when all characters are same.