# 437. Path Sum III

from typing import Optional
from binary_tree import *

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root: TreeNode, target, prev_values=None):
            if not prev_values:
                prev_values = []

            if not root:
                return 0
            
            count = 0
            prev_values.append(root.val)
            # print(prev_values)

            curr_sum = 0
            for v in reversed(prev_values):
                curr_sum += v
                if curr_sum == target:
                    count += 1
            
            count += dfs(root.left, target, prev_values)
            count += dfs(root.right, target, prev_values)
            prev_values.pop()

            return count

        return dfs(root, targetSum)
    

inputs = [
    ([10,5,-3,3,2,None,11,3,-2,None,1], 8, 3),
    ( [5,4,8,11,None,13,4,7,2,None,None,5,1], 22, 3),
]
s = Solution()
for root1, target, result in inputs:
    my_result = s.pathSum(create_tree(root1)[0], target)
    print(my_result, my_result == result)