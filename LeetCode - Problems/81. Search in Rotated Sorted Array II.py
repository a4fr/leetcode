# 81. Search in Rotated Sorted Array II
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2

            if nums[middle] == target:
                return True
            
            # Edge case when we have duplicates in the list
            if nums[start] == nums[middle] == nums[end]:
                start += 1
                end -= 1
                continue
            
            # Left side is sorted
            if nums[start] <= nums[middle]:
                if target < nums[middle] and nums[start] <= target:
                    end = middle -1
                else:
                    start = middle + 1

            # Right side is sorted
            else:
                if target > nums[middle] and target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        # Final result
        return False



inputs = [
    ([2,5,6,0,0,1,2], 0, True),
    ([2,5,6,0,0,1,2], 3, False),
    ([1,0,1,1,1], 0, True),
    ([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13, True),
]

s = Solution()
for nums, target, result in inputs:
    my_result = s.search(nums, target)
    print(nums, target, my_result, my_result==result, sep="\t")
