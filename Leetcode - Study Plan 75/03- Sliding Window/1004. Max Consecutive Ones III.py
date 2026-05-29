# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        count_seen_zeros = 0
        max_cons = 0

        for right, num in enumerate(nums):
            if num == 0:
                count_seen_zeros += 1

            while count_seen_zeros > k:
                if nums[left] == 0:
                    count_seen_zeros -= 1
                left += 1
            max_cons = max(max_cons, right - left + 1)
        
        return max_cons
                




inputs = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
]
s = Solution()
for nums, k, result in inputs:
    my_result = s.longestOnes(nums, k)
    print(my_result, my_result==result)
