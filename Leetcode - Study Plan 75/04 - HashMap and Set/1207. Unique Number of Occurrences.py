# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        num_occurance = {}
        for n in arr:
            if n not in num_occurance:
                num_occurance[n] = 0
            num_occurance[n] += 1
        
        # seen = set()
        # for occ in num_occurance.values():
        #     if occ in seen:
        #         return False
        #     seen.add(occ)
        # return True
        return len(num_occurance) == len(set(num_occurance.values()))

inputs = [
    ([1,2,2,1,1,3], True),
    ([1,2], False)
]
s = Solution()
for arr, result in inputs:
    my_result = s.uniqueOccurrences(arr)
    print(my_result, my_result==result)