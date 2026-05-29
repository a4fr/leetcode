# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        
        start = 0
        end = len(s) - 1
        while start < end:
            for i in range(start, end+1):
                if s[i] in vowels:
                    break
            for j in range(end, start-1, -1):
                if s[j] in vowels:
                    break
            if j >= i:
                s[i], s[j] = s[j], s[i]
            start = i+1
            end = j-1
        return ''.join(s)


inputs = [
    ("IceCreAm", "AceCreIm"),
    ("leetcode", "leotcede"),
]
solution = Solution()
for s, result in inputs:
    my_result = solution.reverseVowels(s)
    print(my_result, my_result==result)

