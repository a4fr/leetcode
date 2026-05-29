# 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        chars = []
        for ch in s:
            if ch == "*":
                chars.pop()
                continue
            chars.append(ch)
        return "".join(chars)


inputs = [
    ("leet**cod*e", "lecoe"),
    ("erase*****", "")
]
s = Solution()
for string, result in inputs:
    my_result = s.removeStars(string)
    print(my_result, my_result==result)