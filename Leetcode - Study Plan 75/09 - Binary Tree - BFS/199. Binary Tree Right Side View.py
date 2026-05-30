# 199. Binary Tree Right Side View

from binary_tree import *
from typing import Optional
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """ Replaced with dequeu to reduce Space Complexity to O(1)
        """
        if not root:
            return []
        nodes = {
            0: deque([root])
        }
        depth = 0
        path = [root.val]
        while depth in nodes:
            childs = deque()
            while nodes[depth]:
                node = nodes[depth].popleft()
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            # Next Depth
            depth += 1
            if childs:
                nodes[depth] = childs
                path.append(childs[-1].val)
        # print(nodes)
        return path
        



inputs = [
    ([1,2,3,None,5,None,4], [1,3,4]),
    ([1,2,3,4,None,None,None,5], [1,3,4,5]),
    ([], []),
]
s = Solution()
for root1, resuilt in inputs:
    my_result = s.rightSideView(None if not root1 else create_tree(root1)[0])
    print(my_result, my_result==resuilt)
