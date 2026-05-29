# 872. Leaf-Similar Trees

from typing import Optional
from binary_tree import *


class Solution:
    def getLeaves(self, root: TreeNode):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.getLeaves(root.left) + self.getLeaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)


inputs = [
    ([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8], True),
    ([1,2,3], [1,3,2], False),
    ([1,2], [2,2], True)
]
s = Solution()
for root1, root2, result in inputs:
    my_result = s.leafSimilar(create_tree(root1)[0], create_tree(root2)[0])
    print(my_result, my_result == result)