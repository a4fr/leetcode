# 215. Kth Largest Element in an Array

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

inputs = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
]
s = Solution()
for nums, k, result in inputs:
    my_result = s.findKthLargest(nums, k)
    print(my_result, my_result==result)