# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        left_product = 1
        right_product = 1
        for i in range(n):
            j = n - i - 1 # index from right
            
            result[i] *= left_product
            left_product *= nums[i]
            
            result[j] *= right_product
            right_product *= nums[j]

        return result


inputs = [
    ([1,2,3,4], [24,12,8,6]),
]
solution = Solution()
for nums, result in inputs:
    my_result = solution.productExceptSelf(nums)
    print(my_result, my_result==result)