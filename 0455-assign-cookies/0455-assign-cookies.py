class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        # Greedy approach trying to give children smaller cookies earlier based on their content, so as to keep larger cookies for further. [Greedy]
        g.sort()  # content needed
        s.sort()  # available cookie sizes
        
        content_children = 0
        cookie_index = 0
        
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        
        return content_children