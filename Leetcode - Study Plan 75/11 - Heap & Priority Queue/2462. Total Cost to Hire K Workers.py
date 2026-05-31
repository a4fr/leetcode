# 2462. Total Cost to Hire K Workers

from heapq import heappop, heappush

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        if k >= n:
            return sum(costs)
        

        left = []
        right = []
        left_index = 0
        right_index = n - 1
        for i in range(candidates):
            if len(left) + len(right) < n:
                heappush(left, costs[left_index])
                left_index += 1
            
            if len(left) + len(right) < n:
                heappush(right, costs[right_index])
                right_index -= 1
            
        
        picked_candidates = 0
        sum_costs = 0
        while picked_candidates < k:
            # print(left, right)
            # print(left_index, right_index)
            if not right or (left and left[0] <= right[0]):
                picked_candidates += 1
                sum_costs += heappop(left)
                if left_index <= right_index:
                    heappush(left, costs[left_index])
                    left_index += 1
            else:
                picked_candidates += 1
                sum_costs += heappop(right)
                if left_index <= right_index:
                    heappush(right, costs[right_index])
                    right_index -= 1

        return sum_costs


        

inputs = [
    ([17,12,10,2,7,2,11,20,8], 3, 4, 11),
    ([1,2,4,1], 3, 3, 4),
    ([18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], 13, 23, 223),
    ([25,65,41,31,14,20,59,42,43,57,73,45,30,77,17,38,20,11,17,65,55,85,74,32,84], 24, 8, 1035),
]
s = Solution()
for costs, k, candidates, result in inputs:
    my_result = s.totalCost(costs, k, candidates)
    print(my_result, my_result == result)