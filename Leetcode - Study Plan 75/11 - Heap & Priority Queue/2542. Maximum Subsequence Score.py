# 2542. Maximum Subsequence Score

import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)
        pairs = sorted(zip(nums2, nums1), reverse=True)
        # print(pairs)

        heap = []
        curr_sum = 0
        answer = 0
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1

            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                answer = max(answer, n2 * curr_sum)
            # print(n2, curr_sum)
        return answer



inputs = [
    ([1,3,3,2], [2,1,3,4], 3, 12),
    ([4,2,3,1,1], [7,5,10,9,6], 1, 30),
    ([2,1,14,12], [11,7,13,6], 3, 168),
]
s = Solution()
for nums1, nums2, k, result in inputs:
    my_result = s.maxScore(nums1, nums2, k)
    print(my_result, my_result==result)