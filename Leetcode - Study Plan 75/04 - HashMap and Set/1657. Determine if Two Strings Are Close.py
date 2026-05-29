# 1657. Determine if Two Strings Are Close
from collections import defaultdict, Counter

class Solution:
    def closeStrings_approach1(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for i in range(len(word1)):
            map1[word1[i]] += 1
            map2[word2[i]] += 1
        # You should have all chars
        for k in map1.keys():
            if k not in map2:
                return False
        
        return sorted(map1.values()) == sorted(map2.values())

    
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 = Counter(word1)
        map2 = Counter(word2)
        for w in map2:
            if w not in map1:
                return False
        return sorted(map1.values()) == sorted(map2.values())

inputs = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
    ("uau", "ssx", False),
    ("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff", False)
]
s = Solution()
for word1, word2, result in inputs:
    my_result = s.closeStrings(word1, word2)
    print(my_result, my_result==result)