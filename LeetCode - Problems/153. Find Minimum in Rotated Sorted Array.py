# 153. Find Minimum in Rotated Sorted Array
# Must be O(log(n))

from typing import List
import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        min_num = math.inf
        while start <= end:
            middle = (start + end) // 2

            # left is sorted
            if nums[start] <= nums[middle]:
                if nums[start] < min_num:
                    min_num = nums[start]
                start = middle + 1
            # Right is sorted
            else:
                if nums[middle] < min_num:
                    min_num = nums[middle]
                end = middle - 1
        return min_num


inputs = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),
    ([2,1], 1),
    ([2,3,4,5,1], 1),
    ([1], 1)
]
s = Solution()
for nums, result in inputs:
    my_result = s.findMin(nums)
    print(nums, my_result, my_result==result)
