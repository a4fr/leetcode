# 2352. Equal Row and Column Pairs
from collections import defaultdict

class Solution:
    def equalPairs_approach1(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        vertical_lists = defaultdict(int)
        for i in range(n):
            v = tuple(grid[j][i] for j in range(n))
            vertical_lists[v] += 1

        # print(vertical_lists)
        cnt = 0
        for row in grid:
            cnt += vertical_lists[tuple(row)]
        return cnt
    
    def equalPairs(self, grid: list[list[int]]) -> int:
        vertical_list = defaultdict(int)
        for col in zip(*grid):
            vertical_list[tuple(col)] += 1
        cnt = 0
        for row in grid:
            cnt += vertical_list[tuple(row)]
        return cnt
    

inputs = [
    ([[3,2,1],[1,7,6],[2,7,7]], 1),
    ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
    ([[3,1,2,2],
      [1,4,4,4],
      [2,4,2,2],
      [2,5,2,2]], 3),
]
s = Solution()
for grid, result in inputs:
    my_result = s.equalPairs(grid)
    print(my_result, my_result==result)