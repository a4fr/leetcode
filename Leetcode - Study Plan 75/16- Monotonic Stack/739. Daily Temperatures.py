# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        
        for i, temp in enumerate(temperatures):
            # print(i, temp)
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i

            stack.append(i)
        return result

inputs = [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0]),
]
s = Solution()
for temperatures, result in inputs:
    my_result = s.dailyTemperatures(temperatures)
    print(my_result, my_result==result)