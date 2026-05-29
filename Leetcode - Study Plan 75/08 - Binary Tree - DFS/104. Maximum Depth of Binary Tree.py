# 104. Maximum Depth of Binary Tree

from typing import Optional
from collections import deque
from binary_tree import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Inputs
inputs =[
    ([3,9,20,None, None,15,7], 3),
    ([1,None,2], 2)
]
s = Solution()
for values, result in inputs:
    nodes = create_tree(values)
    print([str(n) for n in nodes])
    my_result = s.maxDepth(nodes[0])
    print(my_result, my_result == result)
