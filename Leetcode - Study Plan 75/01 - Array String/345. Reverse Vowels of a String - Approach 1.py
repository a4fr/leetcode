# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowels = set('aeiouAEIOU')
        vowel_chars = []
        vowel_indice = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowel_chars.append(s[i])
                vowel_indice.append(i)
        vowel_chars.reverse()
        while vowel_chars:
            index = vowel_indice.pop()
            s[index] = vowel_chars.pop()

        return ''.join(s)


inputs = [
    ("IceCreAm", "AceCreIm"),
    ("leetcode", "leotcede"),
]
solution = Solution()
for s, result in inputs:
    my_result = solution.reverseVowels(s)
    print(my_result, my_result==result)

