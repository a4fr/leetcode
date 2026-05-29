# 1071. Greatest Common Divisor of Strings

import time

class Solution:
    def is_devidable(self, text, sub_text):
        if len(text) % len(sub_text) != 0:
            return False
        
        step = len(sub_text)
        for i in range(0, len(text), step):
            if text[i:i+step] != sub_text:
                return False
            
        return True


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        comm_length = min(len(str1), len(str2))
        for i in range(comm_length, 0, -1):
            sub_str = str1[:i]
            if self.is_devidable(str1, sub_str) and self.is_devidable(str2, sub_str):
                return sub_str
            
        return ""


if __name__ == "__main__":
    problem_inputs = [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("AAAAAB", "AAA", "")
    ]
    solution = Solution()
    time_start = time.time()
    for str1, str2, result in problem_inputs:
        my_result = solution.gcdOfStrings(str1, str2)
        print(str1, str2, my_result, result==my_result, sep="\t")
    print(f"{time.time() - time_start:.9f}")
    # print(solution.is_devidable("ABAB", "ABA"))