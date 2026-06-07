# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        accum_cost = cost[:]
        for i, c in enumerate(cost):
            if i < 2:
                continue
            accum_cost[i] += min(accum_cost[i-2:i])
        # print(accum_cost)

        return min(accum_cost[-2:])


inputs = [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6),
    ([1,0,2,2], 2),
]
s = Solution()
for cost, result in inputs:
    my_result = s.minCostClimbingStairs(cost)
    print(my_result, my_result == result)
