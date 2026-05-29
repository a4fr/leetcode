# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge cases
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        s_i = t_i = 0
        
        while t_i < len(t):            
            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1

            if s_i == len(s):
                return True
        return False

inputs = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("b", "c", False)
]
sol = Solution()
for s, t, result in inputs:
    my_result = sol.isSubsequence(s, t)
    print(my_result, my_result==result)