class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_of(x):
            return Counter(x)
        return count_of(s)  == count_of(t)