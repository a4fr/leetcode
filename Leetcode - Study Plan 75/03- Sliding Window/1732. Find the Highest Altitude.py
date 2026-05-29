# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_sum = 0
        max_gain = 0
        for i, n in enumerate(gain):
            current_sum += n
            max_gain = max(max_gain, current_sum)
        return max_gain

inputs = [
    ([-5,1,5,0,-7], 1),
    ([-4,-3,-2,-1,4,3,2], 0)
]
s = Solution()
for gain, result in inputs:
    my_result = s.largestAltitude(gain)
    print(my_result, my_result==result)