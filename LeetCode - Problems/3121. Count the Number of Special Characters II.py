# 3121. Count the Number of Special Characters II
from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_i = {}
        last_i = {}

        for i, ch in enumerate(word):
            ch_lower = ch.lower()
            if ch.islower():
                last_i[ch] = i
            else:
                if ch_lower not in first_i:
                    first_i[ch_lower] = i
        # print(first_i, last_i)
        result = 0
        for ch in first_i:
            if ch not in last_i:
                continue

            if last_i[ch] < first_i[ch]:
                result += 1

        return result



inputs = [
    ("aaAbcBC", 3),
    ("abc", 0),
    ("AbBCab", 0),
    ("cCceDC", 0),
    ("eEb", 1,)
]
s = Solution()
for word, result in inputs:
    my_result = s.numberOfSpecialChars(word)
    print(my_result, my_result == result)