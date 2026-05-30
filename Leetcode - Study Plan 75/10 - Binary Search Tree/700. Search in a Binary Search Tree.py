# 700. Search in a Binary Search Tree


from binary_tree import *
from typing import Optional
from collections import deque

class Solution:
    def searchBST_approach1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val == val:
                    return node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return None
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            elif node.val > val and node.left:
                q.append(node.left)
            elif node.val < val and node.right:
                q.append(node.right)
        return None


inputs = [
    ([4,2,7,1,3], 2 , 2),
    ([4,2,7,1,3], 5, None),
]
s = Solution()
for root1, val, resuilt in inputs:
    my_result = s.searchBST(None if not root1 else create_tree(root1)[0], val)
    print(my_result, None if my_result is None else my_result.val==resuilt)
