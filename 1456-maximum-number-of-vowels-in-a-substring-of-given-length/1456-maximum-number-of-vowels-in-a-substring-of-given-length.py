class Solution:
    VOWELS = frozenset('aeiou')

    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = curr_vowels = left = 0

        for right in range(len(s)):
            if s[right] in self.VOWELS:
                curr_vowels += 1

            if right - left + 1 > k:
                if s[left] in self.VOWELS:
                    curr_vowels -= 1
                left += 1

            max_vowels = max(max_vowels, curr_vowels)

        return max_vowels