# 1752. Check if Array Is Sorted and Rotated

from typing import List

class Solution:
    def is_sorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return True

    def check(self, nums: List[int]) -> bool:
        if self.is_sorted(nums):
            return True
    
        for i in range(1, len(nums)):
            if self.is_sorted(nums[-i:] + nums[:-i]):
                return True
        
        return False
    

inputs = [
    ([3,4,5,1,2], True),
    ([2,1,3,4], False),
    ([1,2,3], True)
]

s = Solution()
for nums, result in inputs:
    my_result = s.check(nums)
    print(nums, my_result, my_result==result, sep="\t")