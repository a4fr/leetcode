# 11. Container With Most Water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0

        while left < right:
            # print(left, right)
            h = (right - left) * min(height[left], height[right])
            max_height = max(h, max_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_height




inputs = [
    ([1,8,6,2,5,4,8,3,7],  49),
    ([1,1], 1),
    ([1,2,4,3], 4),
]
s = Solution()
for height, result in inputs:
    my_result = s.maxArea(height)
    print(my_result, my_result==result)