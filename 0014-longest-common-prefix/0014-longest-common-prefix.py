class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    # print(i,word,word[i],base,base[i],base[0:i])
                    # taking every char of base, and going with each word in strs, before going to next char. 
                    return base[0:i]

        return base