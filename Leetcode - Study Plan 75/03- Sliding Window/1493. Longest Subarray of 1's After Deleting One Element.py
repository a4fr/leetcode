# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_length = 0
        last_zero = -1
        left = 0
        for i, n in enumerate(nums):
            if n == 0:
                left = last_zero + 1
                last_zero = i
            max_length = max(max_length, i - left)
            
        return max_length


inputs = [
    ([1,1,0,1], 3),
    ([1,1,1], 2),
    ([0,1,1,1,0,1,1,0,1], 5)
]
s = Solution()
for nums, result in inputs:
    my_result = s.longestSubarray(nums)
    print(my_result, my_result==result)