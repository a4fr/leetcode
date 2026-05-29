# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(w for w in words[::-1] if w)


inputs = [
    (" the sky is blue ", "blue is sky the"),
]
solution = Solution()
for s, result in inputs:
    my_result = solution.reverseWords(s)
    print(my_result, my_result==result)

