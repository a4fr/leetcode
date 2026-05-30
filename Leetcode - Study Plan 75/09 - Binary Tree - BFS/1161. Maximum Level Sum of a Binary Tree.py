# 1161. Maximum Level Sum of a Binary Tree

from binary_tree import *
from typing import Optional
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        depth = 1
        max_level_sum = 1
        max_sum = root.val
        while q:
            # Process depth
            sum_this_depth = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_this_depth += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sum_this_depth > max_sum:
                max_level_sum = depth
                max_sum = sum_this_depth
            
            # New depth
            depth += 1
        return max_level_sum


inputs = [
    ([1,7,0,7,-8,None,None], 2),
    ([989,None,10250,98693,-89388,None,None,None,-32127], 2),
]
s = Solution()
for root1, resuilt in inputs:
    my_result = s.maxLevelSum(None if not root1 else create_tree(root1)[0])
    print(my_result, my_result==resuilt)
