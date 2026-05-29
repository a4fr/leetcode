# 283. Move Zeroes

class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                continue

            for j in range(i+1, n):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        insert_i = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[insert_i] = nums[insert_i], nums[i]
                insert_i += 1



inputs = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
]
s = Solution()
for nums, result in inputs:
    my_result = s.moveZeroes(nums)
    print(nums)