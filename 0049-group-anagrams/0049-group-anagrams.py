class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # sort each way and use its key in the dictionary
            key = tuple(sorted(word))
            # key = sorted(word)
            # key = frozenset(sorted(word))
            anagrams[key].append(word)
        
        # Return the values(group of anagrams) from dictionary
        return list(anagrams.values())
    
    # T.C: O(N) for interating strs, sorting each word takes O(klogk), so overall, O(N*klogk)
    # S.C: default dict, with key as tuple, worst case, all may have N different keys, each containing K characters
    
# Key: ('a', 'e', 't'), Anagrams: ['eat', 'tea', 'ate']
# Key: ('a', 'n', 't'), Anagrams: ['tan', 'nat']
# Key: ('a', 'b', 't'), Anagrams: ['bat']

    
    # Topics:
    # 1. defaultdict(list) ensures that anagram_groups[key] returns an empty list if key is not already present.
    # 2.tuple(sorted(word)) creates a key based on the sorted characters of each word.    Tuples are hashable and can be used as keys in dictionaries. This is crucial for creating a mapping between sorted character tuples and lists of anagrams. By using a tuple of sorted characters as a key, the solution ensures that anagrams have the same key and are grouped together.