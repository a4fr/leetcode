# 435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], x[1]-x[0]))
        print(intervals)
        
        interval = intervals[0]
        count_overlapped = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= interval[0] or intervals[i][0] < interval[1]:
                count_overlapped += 1
            else:
                interval = intervals[i]
        return count_overlapped

inputs = [
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2],[1,2],[1,2]], 2),
    ([[1,2],[2,3]], 0),
    ([[1,100],[11,22],[1,11],[2,12]], 2)
]
s = Solution()
for intervals, result in inputs:
    my_result = s.eraseOverlapIntervals(intervals)
    print(my_result, my_result==result)
