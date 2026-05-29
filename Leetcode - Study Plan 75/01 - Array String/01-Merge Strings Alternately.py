# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))

        result = ""
        for i in range(min_length):
            result += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            result += word1[i+1:]
        elif len(word1) < len(word2):
            result += word2[i+1:]
        
        return result


if __name__ == "__main__":
    problem_inputs = [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd")
    ]
    solution = Solution()
    for word1, word2, result in problem_inputs:
        my_result = solution.mergeAlternately(word1, word2)
        print(word1, word2, my_result, result==my_result, sep="\t")