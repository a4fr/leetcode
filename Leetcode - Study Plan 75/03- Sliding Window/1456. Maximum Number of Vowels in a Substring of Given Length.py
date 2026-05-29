# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current_count = 0
        max_count = 0
        for i, ch in enumerate(s):
            if i >=k and s[i-k] in vowels:
                current_count -= 1
            
            if ch in vowels:
                current_count += 1

            max_count = max(max_count, current_count)
            # Edge Case
            if max_count == k:
                break
        return max_count

inputs = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ("leetcode", 3, 2),
]
s = Solution()
for strring, k, result in inputs:
    my_result = s.maxVowels(strring, k)
    print(my_result, my_result==result)