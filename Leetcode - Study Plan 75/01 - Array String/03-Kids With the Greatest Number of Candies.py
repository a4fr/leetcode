# 1431. Kids With the Greatest Number of Candies
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for candy in candies:
            if candy+extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        
        return result
    

inputs = [
    ([2,3,5,1,3], 3, [True,True,True,False,True]),
    ([4,2,1,1,2], 1, [True,False,False,False,False]),
    ([12,1,12], 10, [True, False, True])
]
s = Solution()
for candies, extraCandies, result in inputs:
    my_result = s.kidsWithCandies(candies, extraCandies)
    print(candies, extraCandies, my_result, my_result==result, sep="\t")
