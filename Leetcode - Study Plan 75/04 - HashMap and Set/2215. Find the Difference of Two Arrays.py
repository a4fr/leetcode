# 2215. Find the Difference of Two Arrays
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)

        return [
            list(set_1 - set_2),
            list(set_2 - set_1)
        ]

inputs = [
    ([1,2,3], [2,4,6], [[1,3],[4,6]]),
]
s = Solution()
for nums1, nums2, result in inputs:
    my_result = s.findDifference(nums1, nums2)
    print(my_result, my_result==result)