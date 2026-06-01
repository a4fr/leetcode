# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        result = []
        combinations = self.letterCombinations(digits[1:])
        for w in mapping[digits[0]]:
            result.extend([w + combinations for combinations in combinations])
        return result


inputs = [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("2", ["a","b","c"]),
]
s = Solution()
for digits, result in inputs:
    my_result = s.letterCombinations(digits)
    print(my_result, set(result) == set(my_result))