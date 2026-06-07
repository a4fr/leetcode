# 198. House Robber

class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = nums[:]
        for i in range(len(nums)):
            if i - 3 >= 0:
                dp[i] += max(dp[i-3], dp[i-2])
            elif i - 2 >= 0:
                dp[i] += dp[i-2]

        # print(dp)
        return max(dp[-2:])

inputs = [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
    ([2,1,1,2], 4),
]
s = Solution()
for nums, result in inputs:
    my_result = s.rob(nums)
    print(my_result, my_result==result)