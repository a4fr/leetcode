# 162. Find Peak Element

import math

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            before = -math.inf if i == 0   else nums[i-1]
            after =  -math.inf if i == n-1 else nums[i+1]
            if before < nums[i] > after:
                return i


inputs = [
    ([1,2,3,1], [2]),
    ([1,2,1,3,5,6,4], [1,5]),
]
s = Solution()
for nums, result in inputs:
    my_result = s.findPeakElement(nums)
    print(my_result, my_result in result)