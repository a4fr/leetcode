# 724. Find Pivot Index

class Solution:
    def pivotIndex_approach1(self, nums: list[int]) -> int:
        n = len(nums)
        sum_left = [nums[0]] + [0] * (n-1)
        sum_right = [0] * (n-1) + [nums[-1]]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            j = n-i-1
            sum_left[i] += sum_left[i-1] + num
            sum_right[j] += sum_right[j+1] + nums[j]
        # print(sum_left)
        # print(sum_right)
        
        for i in range(n):
            if sum_left[i] == sum_right[i]:
                return i
        return -1
    
    def pivotIndex_approach2(self, nums: list[int]) -> int:
        n = len(nums)
        sum_left = 0
        sum_right = 0
        sum_total = [0] * n
        for i in range(n):
            j = n-i-1
            sum_left += nums[i]
            sum_right += nums[j]
            sum_total[i] += sum_left
            sum_total[j] -= sum_right
        
        for i, num in enumerate(sum_total):
            if num == 0:
                return i
        return -1
    
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        total_left = 0
        for i, num in enumerate(nums):
            total_left += num
            total_right = total - total_left + num
            # print(i, total_left, total_right)
            if total_left == total_right:
                return i
        return -1


inputs = [
    ([1,7,3,6,5,6], 3),
    ([1,2,3], -1),
    ([2,1,-1], 0),
]
s = Solution()
for gain, result in inputs:
    my_result = s.pivotIndex(gain)
    print(my_result, my_result==result)