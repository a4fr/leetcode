# 392. Is Subsequence
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def isSubsequence_two_pointer(self, s: list[str], t: str) -> bool:
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
    
    def binary_search_gtn(self, arr, target):
        i = bisect_right(arr, target)
        if i == len(arr):
            return None
        return i

    def isSubsequence(self, s: list[str], t: str) -> bool:
        """ Dynamic Programming
        """
        t_map = defaultdict(list)
        for i, ch in enumerate(t):
            t_map[ch].append(i)

        last_i = -1
        for ch in s:
            if ch not in t_map:
                return False
        
            arr = t_map[ch]
            i = self.binary_search_gtn(arr, last_i)
            if i is None:
                return False
            
            last_i = arr[i]
        return True
            

inputs = [
    ("abc", "abcdebd", True),
    ("adc", "abcdebd", False),
]
sol = Solution()

for s, t, result in inputs:
    my_result = sol.isSubsequence(s, t)
    print(my_result, my_result==result)