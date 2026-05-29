# minimum-operations-to-make-array-modulo-alternating-i
import math

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        evens = []
        odds = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        d_even = [n % k for n in evens]
        d_odds = [n % k for n in odds]
        min_steps = math.inf
        for x in range(k):
            for y in range (k):
                if x == y:
                    continue
                new_min_steps = 0
                new_min_steps += sum([min(abs(n-x), k-abs(n-x)) for n in d_even])
                new_min_steps += sum([min(abs(n-y), k-abs(n-y)) for n in d_odds])
                
                # print(x,y, new_min_steps)
                if new_min_steps < min_steps:
                    min_steps = new_min_steps

        return min_steps
    

inputs = [
    ([1,4,2,8], 3, 2),
    ([1,1,1], 3, 1),
    ([63,36,77,19], 4, 3)
]
s = Solution()

# print(s.is_modulo_alternating([1, 5, 1, 8], 3))

for nums, k, result in inputs:
    my_result = s.minOperations(nums, k)
    print(nums, k, my_result, my_result==result, sep="\t")
