# Q3.maximum-path-intersection-sum-in-a-grid

class Solution:
    def maxScore(self, grid) -> int:
        return
    


inputs = [
    ([[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]], 4),
    ([[4,-2,-3],[-1,-3,-1],[-4,2,-1]], 3),
]
s = Solution()

# print(s.is_modulo_alternating([1, 5, 1, 8], 3))

for grid, result in inputs:
    my_result = s.maxScore(grid)
    print(my_result, my_result==result, sep="\t")