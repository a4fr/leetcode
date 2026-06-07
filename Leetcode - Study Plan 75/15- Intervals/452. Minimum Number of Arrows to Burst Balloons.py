# 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])

        point = points[0]
        count_arrows = 1
        for i in range(1, len(points)):
            if points[i][0] <= point[1]:
                continue
            else:
                count_arrows += 1
                point = points[i]
        return count_arrows


inputs = [
    ([[10,16],[2,8],[1,6],[7,12]], 2),
    ([[1,2],[3,4],[5,6],[7,8]], 4),
    ([[1,2],[2,3],[3,4],[4,5]], 2)
]
s = Solution()
for points, result in inputs:
    my_result = s.findMinArrowShots(points)
    print(my_result, my_result==result)