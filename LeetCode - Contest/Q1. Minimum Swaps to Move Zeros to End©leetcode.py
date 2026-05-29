# Q1. Minimum Swaps to Move Zeros to End©leetcode

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i = 0
        j = len(nums) - 1
        swapped = 0
        while i != j:
            if nums[j] == 0:
                j -= 1
                continue

            if nums[i] == 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                swapped += 1
            i += 1
        return swapped

inputs = [
    ([0,1,0,3,12], 2),
    [[0,1,0,2], 1],
    ([0,1,0,3,12], 2),
    ([0,1,0,2], 1),
    ([1,2,0], 0)
]

s = Solution()
for nums, result in inputs:
    my_result = s.minimumSwaps(nums)
    print(nums, my_result, my_result==result, sep="\t")